import streamlit as st
from utils.utils import get_authenticator
from utils.constants import column_mapping, weeks, new_columns, read_google_sheet


if ("authentication_status" not in st.session_state.keys()) or not st.session_state["authentication_status"]:
    st.error('Please come back to main page and login') 
elif st.session_state["authentication_status"] is True:
    st.title('Iscrizioni centro estivo')
    st.button('Aggiorna', on_click=read_google_sheet)
    df = st.session_state['data'].copy()

    posto_col, settimana_col = st.columns(2)

    with posto_col:
        posto = st.selectbox(label='Seleziona posto', options=df['luogo_centro_estivo'].unique())

    with settimana_col:
        week = st.selectbox(label='Seleziona settimana', options=weeks)

    # with periodo_giorno_col:
    #     st.selectbox(label='Seleziona periodo giornata', options=['mattina', 'pomeriggio', 'extra'])

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

    st.markdown("## Extra 16.00 - 18.00")
    df_periodo = df_posto.loc[df_posto['extra'].str.contains(week), ['nome', 'cognome', 'genitore', 'data_nascita', 'cellulare_1']]
    st.table(df_periodo)

    # Display the data in a Streamlit table