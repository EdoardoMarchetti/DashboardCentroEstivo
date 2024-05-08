from turtle import st
import pandas as pd
import toml
import streamlit_authenticator as stauth
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from utils.constants import column_mapping, weeks, new_columns
import json


@st.cache_data
def read_google_sheet():
    print('Leggi dati')
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

    df = pd.DataFrame(data)
    df.columns = new_columns

    df = st.session_state['data']

    return df

#--------------------------------------
#--------- AUTHENTICATION -------------
#--------------------------------------
#MARK: AUTHENTICATION

def get_authenticator():
    # Loading credentials from secrets.toml
    with open('.streamlit/secrets.toml', 'r') as file:
        secrets = toml.load(file)

    # Accessing credentials from the TOML file
    credentials = secrets['credentials']
    cookies = secrets['cookie']
    preauth = secrets['preauthorized']
    

    # Creating the authenticator object
    authenticator = stauth.Authenticate(
        credentials,
        cookies['name'],
        cookies['key'],  # Will be managed automatically
        cookies['expiry_days'],  # Will be managed automatically,
        preauth
    )

    return authenticator