import telebot
import requests
import os
from dotenv import load_dotenv
from pathlib import Path
from commands import get_model_info, list_available_models
from models import Model  # Import the Model class
import json  # Import the json library
import re  # Import the regular expression library

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

# Welcome message for the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    welcome_text = ("Hi, I am your AI assistant! 🤖\n"
                    "Please select a model from the /models list using /models.\n"
                    "To select a model, send its corresponding command (e.g., `/qwq32b`).")
    bot.send_message(chat_id, welcome_text, parse_mode='Markdown')
    # Clear any previously selected model for this chat on /start
    if chat_id in user_selected_models:
        del user_selected_models[chat_id]

# Command to list available models
@bot.message_handler(commands=['models'])
def list_models(message):
    available_models = list_available_models()
    model_list = []
    for model_id, name in available_models:
        cleaned_command = re.sub(r'[\s.:,]', '', f"/{model_id}")
        model_list.append(f"{cleaned_command} {name}")  # Inline code for commands
    bot.send_message(message.chat.id, f"Available models:\n{chr(10).join(model_list)}\n\nTo select a model, send its corresponding command (e.g., `{re.sub(r'[\\s.:,]', '', '/qwq32b')}`).", parse_mode='Markdown')

# Handle all other messages
@bot.message_handler(func=lambda message: True)
def respond_to_message(message):
    user_message = message.text
    chat_id = message.chat.id

    # Exit the chat if the user types 'exit'
    if user_message.lower() == 'exit':
        bot.send_message(chat_id, "Goodbye! Feel free to start a new chat anytime.", parse_mode='Markdown')
        # Clear selected model on exit
        if chat_id in user_selected_models:
            del user_selected_models[chat_id]
        return

    # Check if the user is trying to select a model
    cleaned_user_message = re.sub(r'[\s.:,]', '', user_message)
    selected_model = get_model_info(cleaned_user_message)
    if selected_model:
        # Store the selected model for this chat ID
        user_selected_models[chat_id] = selected_model
        # Send confirmation of the selected model
        description = selected_model.description
        bot.send_message(chat_id, f"You selected: *{selected_model.name}*\n{description}", parse_mode='Markdown')
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

                    # Basic sanitization
                    sanitized_response = bot_response.replace("*", "\\*").replace("_", "\\_").replace("`", "\\`")

                    formatted_response = ""
                    lines = sanitized_response.split('\n')
                    if lines:
                        in_code_block = False
                        code_language = ""
                        for line in lines:
                            stripped_line = line.strip()
                            if stripped_line.startswith("```"):
                                if not in_code_block:
                                    in_code_block = True
                                    match = re.match(r"```(\w+)", stripped_line)
                                    if match:
                                        code_language = match.group(1).lower()
                                        formatted_response += f"```{code_language}\n"
                                    else:
                                        formatted_response += "```\n"
                                else:
                                    in_code_block = False
                                    code_language = ""
                                    formatted_response += "```\n"
                            elif in_code_block:
                                formatted_response += f"{line}\n"
                            elif stripped_line.startswith("**Explanation:**"):
                                formatted_response += "**Explanation:**\n"
                            elif stripped_line.startswith("*"):
                                formatted_response += f"{line}\n"
                            elif stripped_line.startswith("**How to run it:**"):
                                formatted_response += "**How to run it:**\n"
                            elif line.startswith("1. **"):
                                formatted_response += f"{line}\n"
                            elif line.startswith("2. **"):
                                formatted_response += f"{line}\n"
                            elif re.match(r"^\s+\*\s+\*", stripped_line):  # Handle nested bullets
                                formatted_response += f"{line}\n"
                            elif stripped_line == r"\`\`\`python":
                                formatted_response += "```python\n"
                            elif stripped_line == r"print(\"Hello, world!\")":
                                formatted_response += "print(\"Hello, world!\")\n"
                            elif stripped_line == r"\`\`\`":
                                formatted_response += "```\n"
                            elif stripped_line == r"\`\`\`javascript":
                                formatted_response += "```javascript\n"
                            elif stripped_line == r"console.log(\"Hello, World!\");":
                                formatted_response += "console.log(\"Hello, World!\");\n"
                            elif stripped_line == r"\`\`\`html":
                                formatted_response += "```html\n"
                            elif stripped_line == r"<!DOCTYPE html>":
                                formatted_response += "<!DOCTYPE html>\n"
                            elif stripped_line == r"<html>":
                                formatted_response += "<html>\n"
                            elif stripped_line == r"<head>":
                                formatted_response += "<head>\n"
                            elif stripped_line == r" <title>Hello World</title>":
                                formatted_response += " <title>Hello World</title>\n"
                            elif stripped_line == r"</head>":
                                formatted_response += "</head>\n"
                            elif stripped_line == r"<body>":
                                formatted_response += "<body>\n"
                            elif stripped_line == r" <script>":
                                formatted_response += " <script>\n"
                            elif stripped_line == r" console.log(\"Hello, World!\");":
                                formatted_response += " console.log(\"Hello, World!\");\n"
                            elif stripped_line == r" </script>":
                                formatted_response += " </script>\n"
                            elif stripped_line == r"</body>":
                                formatted_response += "</body>\n"
                            elif stripped_line == r"</html>":
                                formatted_response += "</html>\n"
                            else:
                                formatted_response += f"{line}\n"

                    # Split the formatted response into chunks
                    response_chunks = split_message(formatted_response.strip())

                    # Send each chunk as a separate message
                    for chunk in response_chunks:
                        bot.send_message(chat_id, chunk, parse_mode='Markdown')

                except json.JSONDecodeError:
                    bot.send_message(chat_id, "Sorry, I received an invalid JSON response.", parse_mode='Markdown')
            else:
                bot_response = f"Error occurred while processing your request. Status code: {response.status_code}"
                bot.send_message(chat_id, bot_response)
        except Exception as e:
            bot_response = f"An unexpected error occurred: {str(e)}"
            bot.send_message(chat_id, bot_response)
    else:
        # No model selected yet
        bot.send_message(chat_id, "Please select a valid model from the /models list by sending its corresponding command (e.g., `/qwq32b`).", parse_mode='Markdown')

# Start polling
if __name__ == "__main__":
    print("Bot is running and waiting for messages...")
    bot.polling()