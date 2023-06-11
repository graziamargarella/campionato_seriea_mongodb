import streamlit as st
from pymongo import MongoClient
from InitDatabase import initialize_db


# flush database
def flush_database():
    client = MongoClient('mongodb://localhost:27017/')
    client.drop_database('campionato_seriea')
    initialize_db()


st.set_page_config(
    page_title="HomePage",
    page_icon="🏡",
)

st.write("# Introduzione")

st.markdown(
    """
    Tramite quest'interfaccia è possibile interagire con il database MongoDB sviluppato 
    per il progetto di Basi di Dati II da Grazia Margarella e Nicola Pio Santorsa.
    
    Il database contiene i dati relativi alle statistiche del campionato di Serie A 2021-2022.
    I dati sono stati ottenuti integrando i seguenti dataset Kaggle: 
    - [Statistiche per squadra della Serie A 2021-2022](https://www.kaggle.com/datasets/mechatronixs/20212022-season-italy-seriea-team-datasets?select=SerieA-Team-Possession-Stats.csv)
    - [Statistiche per calciatore dei campionati europei 2021-2022](https://www.kaggle.com/datasets/vivovinco/20212022-football-player-stats)
    
    Selezionando una pagina dal menù laterale è possibile visualizzare le query da noi pensate
    per questo progetto.
    """
)

st.write("## Init Database")
st.write('Cliccare su questo pulsante per inizializzare il database')
init_button = st.button('Inizializzazione')
if init_button:
    flush_database()
    st.success('Inizializzazione avvenuta con successo.')
