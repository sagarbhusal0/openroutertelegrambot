# OpenRouter Telegram Bot

The OpenRouter Telegram Bot allows you to interact with various models through Telegram. This bot supports 31 different models, providing a wide range of functionalities and integrations.

## Features

- Supports 31 models for diverse applications.
- Easy integration with Telegram for seamless interaction.
- Customizable and extendable for various use cases.

## Installation Instructions

### Prerequisites

- Python 3.8 or higher
- Telegram account and bot token
- OpenRouter API key

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/openrouter-telegram-bot.git
   cd openrouter-telegram-bot
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**

   Create a `.env` file in the project root directory and add your Telegram bot token and OpenRouter API key:

   ```plaintext
   API_TOKEN=your_telegram_bot_token
   OPENROUTER_API_KEY=your_openrouter_api_key
   ```

4. **Run the Bot**

   ```bash
   python main.py
   ```

## Usage Commands

- `/start`: Start the bot and get a welcome message.
- `/help`: Display a list of available commands.
- `/list_models`: List all 311 supported models.
- `/models: Get detailed information about a specific model.
- `/interact <model_name> <your_message>`: Interact with a specific model by sending a message.

## Example Interactions

To interact with a model named `example_model`, you can use the following command in your Telegram chat with the bot:

```plaintext
/interact example_model Hello, how can you assist me today?
```

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) first.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Support

For any issues or feature requests, please open an issue on the [GitHub repository](https://github.com/yourusername/openrouter-telegram-bot).
