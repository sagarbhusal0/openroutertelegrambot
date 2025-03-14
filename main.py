import telebot
import requests

# Replace '<YOUR_BOT_TOKEN>' with your bot's token
API_TOKEN = '841707184:AAGYFAzRo3cK2fizSe3KV4wvuTWjr7LiSGc'
bot = telebot.TeleBot(API_TOKEN)

# Welcome message for the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = ("Welcome to the AI Chatbot! 🤖\n"
                    "Feel free to ask me anything. Just type your message and I'll respond.\n"
                    "To exit the chat, just type 'exit'.")
    bot.send_message(message.chat.id, welcome_text)

# Handle all other messages
@bot.message_handler(func=lambda message: True)
def respond_to_message(message):
    user_message = message.text
    chat_id = message.chat.id

    # Exit the chat if the user types 'exit'
    if user_message.lower() == 'exit':
        bot.send_message(chat_id, "Goodbye! Feel free to start a new chat anytime.")
        return

    # Call OpenRouter API for chatbot response
    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": "Bearer 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",
            },
            json={
                "model": "deepseek/deepseek-r1:free",
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
            bot_response = response.json().get('choices', [{}])[0].get('message', {}).get('content')
            if not bot_response:  # Check if response is empty
                bot_response = "Sorry, I received an empty response. Please try again."
        else:
            bot_response = f"Error occurred while processing your request. Status code: {response.status_code}"
    except Exception as e:
        bot_response = f"An unexpected error occurred: {str(e)}"

    # Send the response back to the user if it's not empty
    try:
        if bot_response and bot_response.strip():
            bot.send_message(chat_id, bot_response)
        else:
            bot.send_message(chat_id, "Sorry, I couldn't generate a response. Please try again.")
    except telebot.apihelper.ApiTelegramException as e:
        bot.send_message(chat_id, "An error occurred while sending the message. Please try again.")

# Start polling
if __name__ == "__main__":
    print("Deleting webhook...")
    bot.remove_webhook()
    print("Bot is running and waiting for updates...")
    bot.polling()