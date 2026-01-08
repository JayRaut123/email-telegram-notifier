import os
from telegram import Bot

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = int(os.getenv("TELEGRAM_CHAT_ID"))

bot = Bot(token=BOT_TOKEN)

async def send_telegram_message(text):
    await bot.send_message(chat_id=CHAT_ID, text=text)
