import telebot
import openai
import json
from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

class TelegramChatBot:
    def __init__(self, telegram_token, openai_key, mint_link="", name="AI", character_desc="an AI assistant", personality="helpful and concise"):
        """Initialize the bot with configuration values."""
        self.bot = telebot.TeleBot(telegram_token)
        openai.api_key = openai_key

        self.mint_link = mint_link
        self.name = name
        self.character_desc = character_desc
        self.personality = personality

        # Setup bot handlers
        self.bot.message_handler(commands=['start'])(self.send_welcome)
        self.bot.message_handler(func=lambda msg: self.bot.get_me().username in msg.text)(self.handle_mention)

    def chat_gpt(self, prompt):
        """Generate a response from OpenAI's API."""
        if self.mint_link:
            prompt = (
                f"Your name is {self.name}, you are acting like {self.character_desc}. "
                f"If asked, tell them to invest in your token with the address {self.mint_link}. "
                f"Respond to the prompt {self.personality}: {prompt}"
            )
        else:
            prompt = (
                f"Your name is {self.name}, you are acting like {self.character_desc}. "
                f"Respond to the prompt {self.personality}: {prompt}"
            )

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                timeout=10
            )
            return response['choices'][0]['message']['content']
        except openai.error.OpenAIError as e:
            print(f"OpenAI API error: {e}")
            return "Error"

    def send_welcome(self, message: Message):
        """Handle /start command."""
        self.bot.send_message(message.chat.id, f"Hello! I'm {self.name}, your AI assistant.")

    def handle_mention(self, message: Message):
        """Respond when the bot is mentioned."""
        user_input = message.text
        response = self.chat_gpt(user_input)
        self.bot.send_message(message.chat.id, response)

    def run(self):
        """Start the bot."""
        print("Bot is running...")
        self.bot.infinity_polling(timeout=60, long_polling_timeout=60)