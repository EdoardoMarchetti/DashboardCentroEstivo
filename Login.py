
import pandas as pd
import streamlit as st

from streamlit_authenticator.utilities.exceptions import LoginError

from utils.utils import get_authenticator, read_google_sheet







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










