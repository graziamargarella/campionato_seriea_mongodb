import streamlit as st
import pandas as pd
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['campionato_seriea']
collection = db['squadre']

st.title('Statistiche Squadre')

st.write('Squadre con più Gol')
marcatori = pd.DataFrame(collection.find().sort([('Goal_Done',-1)]))
st.table(marcatori[['Squad','Goal_Done']].head())

st.write('Squadre che hanno subito più Gol')
marcatori = pd.DataFrame(collection.find().sort([('Goal_Taken',-1)]))
st.table(marcatori[['Squad','Goal_Taken']].head())

st.write('Squadre Mediamente più Giovani')
squads = pd.DataFrame(collection.find().sort([('Age',1)]))
st.table(squads[['Squad','Age']].head())