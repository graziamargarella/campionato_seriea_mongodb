import pandas as pd
from pymongo import MongoClient
from DataIntegration import clean_data

CONNECTION_STRING = "mongodb://127.0.0.1:27017"


# create MongoDB connection
def get_database():
    client = MongoClient(CONNECTION_STRING)
    return client['campionato_seriea']


def initialize_db():
    # get the db referencce
    db = get_database()
    # create two collections: teams and players
    squadre_calcio = db["squadre"]
    calciatori = db["calciatori"]

    # retrieve clean data and load from the disk
    print('Cleaning data')
    clean_data()
    teams = pd.read_csv("./data/teams.csv")
    teams = teams.drop(["Unnamed: 0"], axis=1)

    players = pd.read_csv("./data/players.csv")
    players = players.drop(["Unnamed: 0"], axis=1)

    # load on the database the data
    teams.reset_index()
    data_dict = teams.to_dict("records")
    squadre_calcio.insert_many(data_dict)

    players.reset_index()
    data_dict = players.to_dict("records")
    calciatori.insert_many(data_dict)
