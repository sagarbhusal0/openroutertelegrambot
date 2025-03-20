import telebot
import requests
import os
from dotenv import load_dotenv
from pathlib import Path
from models import Model, models  # Ensure models is imported correctly
import json
import re
import telegramify_markdown
from telegramify_markdown.customize import get_runtime_config

# Construct the path to the .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Get the Telegram Bot API token from the environment variables
API_TOKEN = os.getenv("API_TOKEN")

# Initialize the Telegram Bot
bot = telebot.TeleBot(API_TOKEN)

# Get the OpenRouter API key from the environment variables
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Dictionary to store the selected model for each chat ID
user_selected_models = {}

def split_message(text, chunk_size=4000):
    """Splits a long text into chunks of a specified size."""
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

# Customize symbols using the deprecated method (temporary workaround)
config = get_runtime_config()
config.markdown_symbol.head_level_1 = "📌"  # Customize the first level title symbol
config.markdown_symbol.link = "🔗"  # Customize the link symbol
config.cite_expandable = True  # Enable expandable citation
config.strict_markdown = True  # Use strict Markdown
config.unescape_html = False  # Do not unescape HTML

# Welcome message for the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    welcome_text = ("Hi, I am your AI assistant! 🤖\n"
                    "Please select a model from the /models list using /models.\n"
                    "To select a model, send its corresponding command (e.g., `/qwq32b`).")
    bot.send_message(chat_id, welcome_text)
    # Clear any previously selected model for this chat on /start
    if chat_id in user_selected_models:
        del user_selected_models[chat_id]

# Command to list available models
@bot.message_handler(commands=['models'])
def list_models(message):
    available_models = list_available_models()
    model_list = []
    for model_id, name in available_models:
        cleaned_command = f"/{model_id}"
        model_list.append(f"{cleaned_command} {name}")
    bot.send_message(message.chat.id, f"Available models:\n{chr(10).join(model_list)}\n\nTo select a model, send its corresponding command (e.g., `/mistralsmall3124binstruct`).")

# Handle all other messages
@bot.message_handler(func=lambda message: True)
def respond_to_message(message):
    user_message = message.text
    chat_id = message.chat.id

    # Exit the chat if the user types 'exit'
    if user_message.lower() == 'exit':
        bot.send_message(chat_id, "Goodbye! Feel free to start a new chat anytime.")
        # Clear selected model on exit
        if chat_id in user_selected_models:
            del user_selected_models[chat_id]
        return

    # Check if the user is trying to select a model
    cleaned_user_message = re.sub(r'[\s.:,]', '', user_message).lower()
    print(f"Debug: cleaned_user_message = {cleaned_user_message}")  # Debug print
    selected_model = get_model_info(cleaned_user_message)

    if selected_model:
        print(f"Debug: Selected model = {selected_model.name}")  # Debug print
        # Store the selected model for this chat ID
        user_selected_models[chat_id] = selected_model
        # Send confirmation of the selected model
        description = selected_model.description
        bot.send_message(chat_id, f"You selected: {selected_model.name}\n{description}")
    elif chat_id in user_selected_models:
        # If a model is already selected, use it for the current message
        selected_model = user_selected_models[chat_id]
        # Call OpenRouter API for chatbot response
        try:
            response = requests.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                },
                json={
                    "model": selected_model.model_id,
                    "messages": [{"role": "user", "content": user_message}],
                    "top_p": 1,
                    "temperature": 0.9,
                    "frequency_penalty": 0,
                    "presence_penalty": 0,
                    "repetition_penalty": 1,
                    "top_k": 0,
                }
            )

            # Parse the response from OpenRouter API
            if response.status_code == 200:
                try:
                    response_json = response.json()
                    bot_response = response_json.get('choices', [{}])[0].get('message', {}).get('content', '')

                    # Telegram MarkdownV2 formatting
                    converted = telegramify_markdown.standardize(bot_response)

                    # Split the formatted response into chunks
                    response_chunks = split_message(converted.strip())

                    # Send each chunk as a separate message
                    for chunk in response_chunks:
                        bot.send_message(chat_id, chunk, parse_mode="MarkdownV2")

                except json.JSONDecodeError:
                    bot.send_message(chat_id, "Sorry, I received an invalid JSON response.")
            else:
                bot_response = f"Error occurred while processing your request. Status code: {response.status_code}"
                bot.send_message(chat_id, bot_response)
        except Exception as e:
            bot_response = f"An unexpected error occurred: {str(e)}"
            bot.send_message(chat_id, bot_response)
    else:
        bot.send_message(chat_id, "Please select a valid model from the /models list by sending its corresponding command (e.g., `/mistralsmall3124binstruct`).")

def get_model_info(user_message):
    """
    Parses the user message and returns the model object if a valid model ID is found.
    """
    for model in models:
        # Process the model ID to match the expected command format
        model_id_command = f"/{model.model_id.split('/')[1].split(':')[0].replace('-', '').replace('.', '').lower()}"
        print(f"Debug: model_id_command = {model_id_command}")  # Debug print
        if user_message == model_id_command:
            return model
    return None

def list_available_models():
    """
    Returns a list of tuples containing the modified model ID and the model name.
    """
    return [(model.model_id.split('/')[1].split(':')[0].replace('-', '').replace('.', '').lower(), f"{model.name.split(':')[0]}: {model.name.split(':')[1]}") for model in models]

# Start polling
if __name__ == "__main__":
    print("Bot is running and waiting for messages...")
    bot.polling()
