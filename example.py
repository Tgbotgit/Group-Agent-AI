from telegram_chatbot import TelegramChatBot

bot = TelegramChatBot(
    telegram_token='telegram_token',  # Correct Telegram bot token (must contain a colon)
    openai_key='OpenAI_API_Key',  # Correct OpenAI API Key
    mint_link='mint_address',  # If no mint address, leave it blank
    name='Trump',  # Bot’s identity
    character_desc='Current President of the United States',  # Describe bot's persona
    personality='confidently and concisely'  # Define bot’s interaction style
)

bot.run()
