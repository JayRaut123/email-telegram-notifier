from dotenv import load_dotenv
load_dotenv()

import asyncio
from read_emails import get_unread_emails, mark_as_read
from telegram_sender import send_telegram_message

async def main():
    emails = get_unread_emails()

    if not emails:
        print("No new emails")
        return

    for email in emails:
        message = (
            f"📧 New Gmail Alert\n\n"
            f"From: {email['sender']}\n"
            f"Subject: {email['subject']}"
        )

        print("Sending Telegram message...")
        await send_telegram_message(message)
        mark_as_read(email["id"])

    print("Done sending messages")

if __name__ == "__main__":
    asyncio.run(main())
