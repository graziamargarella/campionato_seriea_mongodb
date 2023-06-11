import streamlit as st
from pymongo import MongoClient
import pandas as pd

client = MongoClient('mongodb://localhost:27017/')
db = client['campionato_seriea']
collection = db['squadre']

collection.update_many({}, [
    {
        '$addFields': {
            'Points': {'$add': ['$Draw', {'$multiply': ['$Win', 3]}]},
            'DR': {'$subtract': ['$Goal_Done', '$Goal_Taken']}
        }
    }
])

data = list(collection.find().sort([('Points',-1),('DR',-1)]))
st.title('Classifica Serie A')
classifica = {'squadre':[]}
for i in range(len(data)):
    squadra = [{
        'Pos': i+1,
        'Squadra': data[i]['Squad'],
        'PG': 38,
        'V': data[i]['Win'],
        'P': data[i]['Draw'],
        'S': 38 - data[i]['Win'] - data[i]['Draw'],
        'GF': data[i]['Goal_Done'],
        'GS': data[i]['Goal_Taken'],
        'DR': data[i]['DR'],
        'Pt': data[i]['Points']
    }
    ]
    classifica['squadre'].extend(squadra)

df = pd.DataFrame(classifica['squadre'])
df.set_index('Pos', inplace=True)
st.table(df)