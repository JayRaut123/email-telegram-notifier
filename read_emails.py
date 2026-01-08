from gmail_auth import get_gmail_service


def get_unread_emails():
    service = get_gmail_service()

    results = service.users().messages().list(
        userId='me',
        q='is:unread'
    ).execute()

    messages = results.get('messages', [])
    email_data = []

    for msg in messages:
        msg_data = service.users().messages().get(
            userId='me',
            id=msg['id'],
            format='metadata',
            metadataHeaders=['Subject', 'From']
        ).execute()

        headers = msg_data.get('payload', {}).get('headers', [])
        subject = ""
        sender = ""

        for h in headers:
            name = h.get('name', '').lower()
            if name == 'subject':
                subject = h.get('value', '')
            elif name == 'from':
                sender = h.get('value', '')

        email_data.append({
            'id': msg['id'],
            'subject': subject,
            'sender': sender
        })

    return email_data


def mark_as_read(msg_id):
    service = get_gmail_service()
    service.users().messages().modify(
        userId='me',
        id=msg_id,
        body={'removeLabelIds': ['UNREAD']}
    ).execute()
