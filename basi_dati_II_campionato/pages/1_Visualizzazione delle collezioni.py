import streamlit as st
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['campionato_seriea']
collection_1 = db['squadre']
collection_2 = db['calciatori']

st.title('Visualizzazione Collezioni')
st.write("## Collezione Squadre")
data = collection_1.find()
st.table(data)

st.write("## Collezione Calciatori")
data = collection_2.find()
st.table(data)
