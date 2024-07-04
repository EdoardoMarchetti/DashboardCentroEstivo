import pandas as pd
import streamlit as st
from Login import read_google_sheet
from utils.utils import get_authenticator
from utils.constants import column_mapping, weeks, new_columns


if ("authentication_status" not in st.session_state.keys()) or not st.session_state["authentication_status"]:
    st.error('Please come back to main page and login') 
elif st.session_state["authentication_status"] is True:
    st.title('Informazioni iscritto')
    df = st.session_state['data'].copy()
    if st.button(label='Aggiorna dati'):
        st.session_state['data'] = read_google_sheet()
    df['nome_completo'] = df[['nome', 'cognome']].apply(lambda x : f"{x['nome']} {x['cognome']}", axis=1)

    iscritto = st.selectbox(label='Selezione iscritto', options=sorted(df['nome_completo'].unique()))
    iscritto_record = df.loc[df.nome_completo == iscritto].iloc[-1]
    st.divider()

    st.markdown(f"## {iscritto_record['nome_completo']}")
    
    st.markdown("#### Dati anagrafici")
    st.markdown(f"**Nato/a a** {iscritto_record['luogo_nascita']} **il** {iscritto_record['data_nascita']}")
    st.markdown(f"**Residente** a {iscritto_record['residenza']}")
    st.markdown(f"**Codice fiscale** {iscritto_record['codice_fiscale']}")
    st.markdown(f"**Genitore** {iscritto_record['genitore']}")
    st.markdown(f"**Già socio** {iscritto_record['gia_socio']}")

    st.divider()

    st.markdown("#### Periodo di iscrizione")
    data = {
        '8:00-13:00': ['x' if w in iscritto_record['mattina'] else '' for w in weeks ],
        '8:00-16:00' : ['x' if w in iscritto_record['mattina_pomeriggio'] else '' for w in weeks],
        '16:00-18:00': ['x' if w in iscritto_record['extra'] else '' for w in weeks],
        }
    
    presenze_df = pd.DataFrame(data, index=weeks)
    
    st.table(presenze_df)
    piscina = 'Aderisco' if iscritto_record['Piscina'].lower()=='aderisco' else 'Non Aderisco'
    st.markdown(f"**Piscina** {piscina}")
    st.markdown(f"**Metodo pagamento** {iscritto_record['modalita_pagamento']}")

    st.divider()

    st.markdown("#### Certificazione buona salute")
    st.markdown(f"**Dichiarazione buona salute** {iscritto_record['salute_figlio']}")
    st.markdown(f"**Allergie alimentari** {iscritto_record['allergie_alimentari']}")
    st.markdown(f"**Allergie farmaci** {iscritto_record['allergie_farmaci']}")
    st.markdown(f"**Assunzione farmaci** {iscritto_record['assunzione_farmaci']}")
    st.markdown(f"**Altre esigenze** {iscritto_record['altre_esigenze']}")

    st.divider()

    st.markdown("#### Contatti e delegati")
    st.markdown(f"**Email** {iscritto_record['email']}")
    st.markdown(f"**Cellulare 1** {iscritto_record['cellulare_1']}")
    st.markdown(f"**Cellulare 2** {iscritto_record['cellulare_2']}")
    st.markdown(f"**Cellulare 3** {iscritto_record['cellulare_3']}")
    st.markdown(f"")
    st.markdown(f"**Persona 1** {iscritto_record['persona_1']}")
    st.markdown(f"**Persona 2** {iscritto_record['persona_2']}")
    st.markdown(f"**Persona 3** {iscritto_record['persona_3']}")


    st.divider()

    st.markdown("#### Consensi")
    st.markdown(f"**Liberatoria** {iscritto_record['responsabilita']}")
    st.markdown(f"**Trattamento dati personali** {iscritto_record['consenso_trattamento_dati']}")
    


