Group Agent AI
Overview
This Telegram AI agent is designed to seamlessly interact in group chats, acting as a digital assistant with a configurable personality and character description. It leverages advanced natural language processing, allowing dynamic and context-aware responses. Additionally, it can be configured to promote a specific mint address when prompted.

Installation
Step 1: Install the Package
Ensure you have git and pip installed, then run:

pip install git+https://github.com/Tgbotgit/Group-Agent-AI.git
Setup
Step 2: Configure the AI Agent
Generate a Telegram Bot Token:

Go to Telegram and start a chat with BotFather.
Use /newbot to create a bot and obtain your bot token.
Run /setjoingroup to allow the bot to participate in group chats.
Run /setprivacy and disable privacy mode so it can read messages.
Generate an OpenAI API Key:

Go to OpenAI's API platform and sign in or create an account.
Navigate to the API key section and generate a new key.
Copy and securely store this key for use in the bot.
Running the AI Agent
Once you have the necessary credentials, initialize and run the AI-powered agent using the script below:

from telegram_chatbot import TelegramChatBot

bot = TelegramChatBot(
    telegram_token='TELEGRAM_BOT_TOKEN', # Generated via BotFather
    openai_key='OPENAI_API_KEY', # Generated from OpenAI
    mint_link='MINT_LINK', # Input mint address for bot to promote, else leave blank ('')
    name='name', # Define the bot’s identity
    character_desc='character_description', # Describe the bot’s persona
    personality='personality' # Define its interaction style, e.g., 'analytical, professional, engaging'
)

bot.run()
Usage
Step 3: Deploy and Interact with the AI Agent
Add the bot to a Telegram group.
Mention the bot using @your_bot_username followed by a message.
The AI agent will process the request using OpenAI’s API and respond accordingly.
Support
For issues or inquiries, contact the repository owner or open an issue on GitHub.