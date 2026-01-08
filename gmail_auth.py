import os
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

TOKEN_FILE = 'token.pickle'
CREDENTIALS_FILE = 'credentials.json'


def get_gmail_service():
    creds = None

    # 1️⃣ Load existing token
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as token:
            creds = pickle.load(token)

    # 2️⃣ If token exists but expired → refresh
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())

    # 3️⃣ If token DOES NOT exist → STOP (no browser on Railway)
    if not creds or not creds.valid:
        raise Exception(
            "Gmail token not found or invalid. "
            "Authorize locally first by running worker.py on your laptop."
        )

    # 4️⃣ Build Gmail service
    service = build('gmail', 'v1', credentials=creds)
    return service
