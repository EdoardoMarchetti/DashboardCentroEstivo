column_mapping = {
    'Informazioni cronologiche': 'cronologia',
    'Il sottoscritto/a (indicare nome e cognome del genitore)': 'genitore',
    'Nome': 'nome',
    'Cognome': 'cognome',
    'Indicare il luogo del centro estivo': 'luogo_centro_estivo',
    'Nato/a a': 'luogo_nascita',
    'Data di nascita figlio/a': 'data_nascita',
    'Residenza figlio/a (formato città, via, numero civico, cap)': 'residenza',
    'CODICE FISCALE': 'codice_fiscale',
    'Già socio': 'gia_socio',
    'Dal Lunedi al Venerdì dalle 08.00 alle 13.00\nTariffe con decorrenza dalla settimana:\nQuota settimanale senza pranzo merenda da casa 65 euro, sconto secondo figlio 5 euro. \nQuota giornaliera 20 euro. \nSelezionare settimana di interesse': 'mattina',
    'Dal Lunedi al Venerdì dalle 08.00 alle 16.00 \nTariffa comprensiva del PRANZO, merenda da casa, decorrenza dalla settimana.\nQuota settimanale 90 euro, sconto secondo figlio 5 euro.\nQuota giornaliera 25 euro. \nSelezionare settimana di interesse ': 'mattina_pomeriggio',
    'Dal Lunedi al Venerdì dalle 16.00 alle 18.00 \nCosto 20 euro a settimana in più da corrispondere direttamente alla maestra Martina.\nSelezionare settimana di interesse. \n\nSELEZIONARE SOLO PER IL CENTRO ESTIVO OASI VERDE CASTELLO DELLE FORME. ': 'extra',
    'Selezionare la modalità di pagamento': 'modalita_pagamento',
    'Allergie alimentari. \nSe si, indicare quali \nSe no, scrivere "no"': 'allergie_alimentari',
    'Allergie ai farmaci \nSe si, indicare quali \nSe no, scrivere "no" ': 'allergie_farmaci',
    'Cellulare 1': 'cellulare_1',
    'Cellulare 2': 'cellulare_2',
    'Cellulare 3': 'cellulare_3',
    'Persona 1': 'persona_1',
    'Persona 2': 'persona_2',
    'Persona 3': 'persona_3',
    'CONSENSO AL TRATTAMENTO DEI DATI \nL’interessato dichiara di aver preso atto dell’informativa resa ai sensi dell’art. 13 del GDPR 679/2016 sul trattamento dei suoi dati, ivi compreso il trattamento di “categorie particolari di dati” ed acconsente, inoltre, all’utilizzo ed alla pubblicazione di video e fotografie, realizzati allo scopo di documentare e rappresentare le attività dell’Associazione. ': 'consenso_trattamento_dati',
    'Il sottoscritto genitore dichiara che il/la proprio/a figlio/a gode di buona salute psico-fisica. ': 'salute_figlio',
    'Io sottoscritto/a genitore sollevo gli organizzatori dell’evento da qualsiasi responsabilità civile e/o penale che possa derivare al partecipante a causa di infortuni e/o danni a persone e cose e/o smarrimento di effetti personali a proprio discapito o di terzi. ': 'responsabilita',
    'Assunzione farmaci': 'assunzione_farmaci',
    'ALTRE ESIGENZE PARTICOLARI': 'altre_esigenze'
}

new_columns = list(column_mapping.values())

weeks = [
    'dal 24 giugno al 28 giugno',
    'dal 1 luglio al 5 luglio',
    'dal 8 luglio al 12 luglio',
    'dal 15 luglio al 19 luglio',
    'dal 22 luglio al 26 luglio',
    'dal 29 luglio al 2 agosto',
    'dal 5 agosto all’ 9 agosto',
    'dal 19 agosto al 23 agosto',
    'dal 26 agosto al 30 agosto',
    'dal 2 settembre al 6 settembre',
]