from read_emails import get_unread_emails, mark_as_read
from whatsapp import send_whatsapp
import time

while True:
    emails = get_unread_emails()

    for email in emails:
        message = f"📧 New Email\nFrom: {email['sender']}\nSubject: {email['subject']}"
        send_whatsapp(message)
        mark_as_read(email['id'])

    time.sleep(60)  # check every 1 minute
