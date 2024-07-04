import pandas as pd
import streamlit as st
from utils.utils import get_authenticator
from utils.constants import column_mapping, weeks, new_columns
from Login import read_google_sheet


if ("authentication_status" not in st.session_state.keys()) or not st.session_state["authentication_status"]:
    st.error('Please come back to main page and login') 
elif st.session_state["authentication_status"] is True:
    if 'data' not in st.session_state.keys():
        st.session_state['data'] = pd.DataFrame(read_google_sheet())
    st.title('Iscrizioni centro estivo')

    if st.button(label='Aggiorna dati'):
        st.session_state['data'] = read_google_sheet()
        
    df = st.session_state['data'].copy()

    

    posto_col, settimana_col = st.columns(2)

    with posto_col:
        posto = st.selectbox(label='Seleziona posto', options=df['luogo_centro_estivo'].unique())

    with settimana_col:
        week = st.selectbox(label='Seleziona settimana', options=weeks)



    st.divider()

    df_posto = df.loc[
        (df['luogo_centro_estivo'] == posto)
    ]




    st.markdown("## Mattina 8:00 - 13:00")
    df_periodo = df_posto.loc[df_posto['mattina'].str.contains(week), ['nome', 'cognome', 'genitore', 'data_nascita', 'cellulare_1']]
    st.table(df_periodo)

    st.markdown("## Pomeriggio 8:00 - 16:00")
    df_periodo = df_posto.loc[df_posto['mattina_pomeriggio'].str.contains(week), ['nome', 'cognome', 'genitore', 'data_nascita', 'cellulare_1']]
    st.table(df_periodo)

    st.markdown("## Extra 16:00 - 18:00")
    df_periodo = df_posto.loc[df_posto['extra'].str.contains(week), ['nome', 'cognome', 'genitore', 'data_nascita', 'cellulare_1']]
    st.table(df_periodo)

    # Display the data in a Streamlit table