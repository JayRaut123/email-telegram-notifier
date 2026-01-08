from telegram import Bot
import asyncio

BOT_TOKEN = "8316567130:AAE_tXUBmvk3HGggtuYwSchfsqJ1bAYunqU"

async def main():
    bot = Bot(BOT_TOKEN)
    updates = await bot.get_updates()
    for u in updates:
        print(u.message.chat.id)

asyncio.run(main())
