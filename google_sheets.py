import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
from google.oauth2 import service_account

load_dotenv()

spreadsheet_id = os.getenv('SPREADSHEET_ID')

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

credentials_file = 'credentials.json'

def write_to_sheet(sheet_name, range, values):
    creds = None
    if os.path.exists(credentials_file):
        creds = service_account.Credentials.from_service_account_file(
            credentials_file, scopes=SCOPES)
    if creds and spreadsheet_id:
        service = build('sheets', 'v4', credentials=creds)

        body = {
            "values": values
        }

        service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range=sheet_name+'!' + range,  # Adjust range for your data
            valueInputOption='USER_ENTERED',
            body=body).execute()

        print('Data written to sheet!')
    else:
        print('You need to set up your Google Cloud Platform project first.')
