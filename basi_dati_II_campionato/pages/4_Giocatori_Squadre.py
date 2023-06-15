import streamlit as st
import pandas as pd
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['campionato_seriea']
calciatori = db['calciatori']

squads = calciatori.distinct("Squad")

option = st.selectbox(
    'Seleziona la squadra di cui vuoi conoscere i giocatori',
    squads)

filtered = pd.DataFrame(calciatori.find({"Squad": option}).sort("Player", 1))
filtered = filtered.drop(["_id"], axis=1)

st.table(filtered)
