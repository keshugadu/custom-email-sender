import pandas as pd
from google.oauth2.service_account import Credentials
import gspread

def load_data_from_csv(file_path):
    return pd.read_csv(file_path)

def load_data_from_google_sheet(sheet_url, creds_file = "C:\\Users\\Lenovo\\Downloads\\custom email sender\\creds.json"):
    creds = Credentials.from_service_account_file(creds_file, scopes=["https://www.googleapis.com/auth/spreadsheets"])
    client = gspread.authorize(creds)
    sheet = client.open_by_url(sheet_url).sheet1
    data = sheet.get_all_records()
    return pd.DataFrame(data)