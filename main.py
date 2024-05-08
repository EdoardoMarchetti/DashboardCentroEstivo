import json
import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def read_google_sheet():
    # Define the scope of the Google Sheet
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    # Load credentials from the TOML file
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(st.secrets["google_secret"].to_dict(), scope)

    # Authenticate using the credentials
    gc = gspread.authorize(credentials)

    # Open the Google Sheet by its title
    sheet = gc.open('Iscrizioni centro estivo (Risposte)').sheet1

    # Read all data from the sheet
    data = sheet.get_all_records()

    return data




# Title of the Streamlit app
st.title('Google Sheets Data Reader')

# Read data from the Google Sheet
sheet_data = read_google_sheet()

# Display the data in a Streamlit table
st.write(sheet_data)
