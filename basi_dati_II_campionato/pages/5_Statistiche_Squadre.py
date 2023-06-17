import streamlit as st
import pandas as pd
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['campionato_seriea']
collection = db['squadre']

st.title('Statistiche Squadre')

option = st.selectbox(
    'Seleziona la squadra di cui vuoi conoscere i giocatori',
    ('Goal Fatti','Goal Subiti','Età'))

order = -1
if option == "Goal Fatti" :
    param = 'Goal_Done'
elif option == "Goal Subiti" :
    param = 'Goal_Taken'
else :
    param = 'Age'
    order = 1

filtered = pd.DataFrame(collection.find().sort(param, order))
st.table(filtered[['Squad',param]])

