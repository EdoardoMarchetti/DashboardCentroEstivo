import json
import pandas as pd
import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from utils.constants import column_mapping, weeks, new_columns
from streamlit_authenticator.utilities.exceptions import LoginError

from utils.utils import get_authenticator 


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
    df = df.rename(columns=column_mapping)
    df = df.astype(dtype=str)
    

    return df





authenticator = get_authenticator()

# Creating a login widget
try:
   authenticator.login()
except LoginError as e:
   st.error(e)

if st.session_state["authentication_status"]:
    st.title("Iscrizioni Centro Estivo")
    st.markdown("Usa questa pagina per monitorare in base a luogo e settimana gli iscritti")

    st.title("Info Iscritto")
    st.markdown("Usa questa pagina per leggere le informazioni dell'iscritto")

if 'data' not in st.session_state.keys():
    st.session_state['data'] = pd.DataFrame(read_google_sheet())












