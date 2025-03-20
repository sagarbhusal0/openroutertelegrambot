# OpenRouter Telegram Bot

The OpenRouter Telegram Bot allows you to interact with various models through Telegram. This bot supports 31 different models, providing a wide range of functionalities and integrations.

## Features

- Supports 33 models for diverse applications.
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
- `/models`: List all 33 supported models.




# AI Model List

This Telegram OpenRouter bot contains a list of various AI models along with brief descriptions. Each model is numbered for easy reference.

## AI Models

1. **Google: Gemma 3 4B (free)** (`google/gemma-3-4b-it:free`)
   - Description: Gemma 3 introduces multimodality, supporting vision-language input and text outputs.

2. **Qwen: QWQ 32B (free)** (`qwen/qwq-32b:free`)
   - Description: A distilled version of the DeepSeek-R1 model, optimized for reasoning domains like mathematics, coding, and logic.

3. **RekaAI: Reka Flash 3 (free)** (`rekaai/reka-flash-3:free`)
   - Description: Experimental release with limited multilingual understanding capabilities.

4. **Google: Gemma 3 12B (free)** (`google/gemma-3-12b-it:free`)
   - Description: Part of the Gemma 3 family, offering improved math, reasoning, and chat capabilities.

5. **MoonShotAI: MoonLight 16B A3B Instruct (free)** (`moonshotai/moonlight-16b-a3b-instruct:free`)
   - Description: Optimized for low-latency performance across common AI tasks.

6. **NousResearch: DeepHermes 3 Llama 3 8B Preview (free)** (`nousresearch/deephermes-3-llama-3-8b-preview:free`)
   - Description: A preview model based on Llama 3, designed for high-quality dialogue use cases.

7. **Qwen: QWQ 32B Preview (free)** (`qwen/qwq-32b-preview:free`)
   - Description: Preview version of Qwen's 32B parameter model.

8. **DeepSeek: DeepSeek R1 Zero (free)** (`deepseek/deepseek-r1-zero:free`)
   - Description: Fully open-source model with strong performance in reasoning domains.

9. **DeepSeek: DeepSeek Chat (free)** (`deepseek/deepseek-chat:free`)
   - Description: Open-source model optimized for chat applications.

10. **Google: Gemini 2.0 Flash Thinking Experimental (free)** (`google/gemini-2.0-flash-thinking-exp:free`)
    - Description: Experimental version of Gemini Flash optimized for speed and efficiency.

11. **DeepSeek: DeepSeek R1 (free)** (`deepseek/deepseek-r1:free`)
    - Description: Open-sourced model with fully open reasoning tokens.

12. **Sophosympatheia: Rogue Rose 103B v0.2 (free)** (`sophosympatheia/rogue-rose-103b-v0.2:free`)
    - Description: A large language model with strong reasoning capabilities.

13. **Google: Gemini 2.0 Flash Experimental (free)** (`google/gemini-2.0-flash-exp:free`)
    - Description: Experimental version of Gemini Flash with reduced latency.

14. **Google: Gemma 2 27B (free)** (`google/gemma-2-27b-it:free`)
    - Description: Advanced open-source language model built using Google's research.

15. **Google: Gemini Experimental 1206 (free)** (`google/gemini-exp-1206:free`)
    - Description: Experimental release (December 6, 2024) of Gemini.

16. **Meta-Llama: Llama 3.3 70B Instruct (free)** (`meta-llama/llama-3.3-70b-instruct:free`)
    - Description: Meta's latest class of model optimized for high-quality dialogue.

17. **MistralAI: Mistral Small 24B Instruct 2501 (free)** (`mistralai/mistral-small-24b-instruct-2501:free`)
    - Description: A 24B-parameter language model optimized for low-latency performance.

18. **DeepSeek: DeepSeek R1 Distill Qwen 32B (free)** (`deepseek/deepseek-r1-distill-qwen-32b:free`)
    - Description: Distilled version of Qwen 2.5 32B, achieving state-of-the-art results.

19. **DeepSeek: DeepSeek R1 Distill Qwen 14B (free)** (`deepseek/deepseek-r1-distill-qwen-14b:free`)
    - Description: Distilled version of Qwen 2.5 14B, outperforming OpenAI's o1-mini.

20. **DeepSeek: DeepSeek R1 Distill Llama 70B (free)** (`deepseek/deepseek-r1-distill-llama-70b:free`)
    - Description: Distilled version of Llama 70B, optimized for reasoning tasks.

21. **Google: Gemini 2.0 Flash Lite Preview (February 05, 2024)** (`google/gemini-2.0-flash-lite-preview-02-05:free`)
    - Description: Preview version of Gemini Flash Lite with faster time-to-first-token.

22. **Qwen: Qwen 2.5 VL 72B Instruct (free)** (`qwen/qwen2.5-vl-72b-instruct:free`)
    - Description: Multimodal LLM from the Qwen Team with enhancements for vision-language tasks.

23. **Qwen: Qwen 2.5 Coder 32B Instruct (free)** (`qwen/qwen-2.5-coder-32b-instruct:free`)
    - Description: Specialized for coding tasks, part of the Qwen 2.5 family.

24. **NVIDIA: Llama 3.1 Nemotron 70B Instruct (free)** (`nvidia/llama-3.1-nemotron-70b-instruct:free`)
    - Description: Optimized for natural language tasks and multiturn text/code chat.

25. **Google: Gemma 2 9B (free)** (`google/gemma-2-9b-it:free`)
    - Description: Open-source language model suitable for text generation tasks.

26. **Meta-Llama: Llama 3.2 3B Instruct (free)** (`meta-llama/llama-3.2-3b-instruct:free`)
    - Description: Smaller variant of Meta's Llama 3 series, optimized for dialogue.

27. **Meta-Llama: Llama 3.2 1B Instruct (free)** (`meta-llama/llama-3.2-1b-instruct:free`)
    - Description: Compact version of Llama 3, designed for lightweight use cases.

28. **Meta-Llama: Llama 3.2 11B Vision Instruct (free)** (`meta-llama/llama-3.2-11b-vision-instruct:free`)
    - Description: Vision-enabled variant of Llama 3, supporting multimodal tasks.

29. **Qwen: Qwen 2.5 72B Instruct (free)** (`qwen/qwen-2.5-72b-instruct:free`)
    - Description: Latest series of Qwen large language models with significant improvements.

30. **Qwen: Qwen 2 7B Instruct (free)** (`qwen/qwen-2-7b-instruct:free`)
    - Description: Transformer-based model excelling in language understanding and coding.

31. **MistralAI: Mistral Nemo (free)** (`mistralai/mistral-nemo:free`)
    - Description: Multimodal model supporting image and video inputs.

32. **MistralAI: Mistral Small 3.1 24B Instruct (free)** (`mistralai/mistral-small-3.1-24b-instruct:free`)
    - Description: Mistral Small 3.1 24B Instruct is an upgraded variant of Mistral Small 3 (2501), featuring 24 billion parameters with advanced multimodal capabilities. It provides state-of-the-art performance in text-based reasoning and vision tasks, including image analysis, programming, and mathematical reasoning.

33. **Open-R1: OlympicCoder 7B (free)** (`open-r1/olympiccoder-7b:free`)
    - Description: OlympicCoder-7B is an open-source language model fine-tuned on the CodeForces-CoTs dataset, consisting of nearly 100,000 high-quality chain-of-thought examples from competitive programming contexts.

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) first.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Support

For any issues or feature requests, please open an issue on the [GitHub repository](https://github.com/yourusername/openrouter-telegram-bot).
