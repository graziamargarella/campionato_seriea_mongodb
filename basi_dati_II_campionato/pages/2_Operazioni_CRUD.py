import streamlit as st
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['campionato_seriea']
collection = db['calciatori']

st.title('Operazioni CRUD')
st.write("## Create")
with st.form(key='insert_form'):
    player = st.text_input('Player')
    nation = st.text_input('Nation')
    pos = st.text_input('Pos')
    squad = st.text_input('Squad')
    age = st.number_input('Age')
    submit_button1 = st.form_submit_button('Insert')
    if submit_button1:
        if len(nation) == 3 and player != "" and pos != "" and squad != "" and age != 0:
            document = {
                'Player': player,
                'Nation': nation,
                'Pos': pos,
                'Squad': squad,
                'Age': age
            }
            result = collection.insert_one(document)
            st.success(f"Document inserted with ID: {result.inserted_id}")
        else:
            st.error('Inserisci i valori in tutti i campi (Nazione Minimo 3 caratteri)')



st.write("## Read")
st.write('Cerca Giocatori utilizzando i 3 campi o solamente alcuni di questi')
with st.form(key='Search-Form'):
    player = st.text_input('Player')
    nation = st.text_input('Nation')
    squad = st.text_input('Squad')
    submit_button2 = st.form_submit_button('Search')
    query = {
        '$and': [
            {'Player': {'$regex': player, '$options' : 'i'}},
            {'Nation': {'$regex': nation, '$options' : 'i'}},
            {'Squad': {'$regex': squad, '$options' : 'i'}},
        ],

    }
    if submit_button2:
        data = collection.find(query)
        st.table(data)


st.write("## Update")
player_to_update = st.text_input('Player da aggiornare')
new_squad = st.text_input('Nuova squadra')
update_button = st.button('Update')
if update_button and new_squad and player_to_update:
    collection.update_many({'Player': player_to_update}, {'$set': {'Squad': new_squad}})
    st.success('Update avvenuto con successo.')
    data = collection.find({'Player': player_to_update})
    st.table(data)

st.write("## Delete")
player_to_delete = st.text_input('Player da cancellare')
delete_button = st.button('Cancella')
if delete_button:
    collection.delete_many({'Player': player_to_delete})
    st.success('Cancellazione avvenuta con successo.')
