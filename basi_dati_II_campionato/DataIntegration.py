import pandas as pd

# Import dataset, columns drop, fix data
# SQUAD STATS
columns_names_dict = {
    "CrdY": "Yellow_Card", "CrdR": "Red_Card", "Sh": "Total_Shoot", "SoT": "Shoot_Target",
    "Shd90": "Shoot_90min", "SoTd90": "Shoot_Target_90min", "GdSh": "Goal_Shot", "GdSoT": "Goal_Shot_Target",
    "Poss": "Possession", "TotTouc": "Total_Touches", "SuccDrib": "Dribbling_Successful",
    "TotDistCarr": "Total_Distance", "DisCarr": "Lose_Ball", "SucRec": "Successful_Pass", "Ast": "Total_Assist",
    "KP": "Key_Passes", "CrsPA": "Crosses", "W": "Win", "D": "Draw", "GF": "Goal_Done", "GA": "Goal_Taken",
    "TotTkl": "Total_Tackles", "TotTklW": "Tackles_Won", "PressTot": "Total_Pressing",
    "SuccPress": "Pressing_Successful", "Int": "Interception", "CmpTot": "Pass_Completed"
}


def import_squad_stats():
    df_standard_stats = pd.read_csv('./data/SerieA-Team-Standard-Stats.csv', sep=';',
                                    encoding='latin-1')
    df_standard_stats = df_standard_stats.drop(
        ['Poss', 'PerGls', 'PerAst', 'PerGmPK', 'PerPK', 'PerPKatt', 'Per90Gls', 'Per90Ast', 'PerGpA', 'PerGmPK.1',
         'PerGpAmPK', 'PerxG', 'PernpxG', 'PerxA', 'PernpxGpxA', 'Per90xG', 'Per90xA', 'Per90xGpxA', 'Per90npxG',
         'Per90npxGxA'], axis=1)

    df_shooting_stats = pd.read_csv('./data/SerieA-Team-Shooting-Stats.csv', sep=';',
                                    encoding='latin-1')
    df_shooting_stats = df_shooting_stats.drop(
        ['Gls', 'SoTRt', 'Dist', 'FK', 'PK', 'PKatt', 'xG', 'npxG', 'npxGdSh', 'GmxG', 'npGmxG'], axis=1)
    df_possession_stats = pd.read_csv('./data/SerieA-Team-Possession-Stats.csv',
                                      sep=';', encoding='latin-1')
    df_possession_stats = df_possession_stats.drop(
        ['DefPenTouc', 'Def3rdTouc', 'Mid3rdTouc', 'Att3rdTouc', 'AttPenTouc', 'LiveTouc', 'AttDrib', 'SuccDribRt',
         'Megs',
         'TotCarr', 'PrgDistCarr', 'ProgCarr', '1/3Carr', 'CPA', 'MisCarr', 'TargRec', 'RecRt', 'ProgRec'], axis=1)
    df_passing_stats = pd.read_csv('./data/SerieA-Team-Passing-Stats.csv', sep=';',
                                   encoding='latin-1')
    df_passing_stats = df_passing_stats.drop(
        ['AttTot', 'TotCmpRt', 'TotDist', 'PrgDist', 'CmpSh', 'AttSh', 'CmpShRt', 'CmpMed', 'AttMed', 'CmpMedRt',
         'CmpLng',
         'AttLng', 'CmpLngRt', 'xA', '1-Mar', 'PPA', 'ProgPs', 'AmxA'], axis=1)
    df_league_stats = pd.read_csv('./data/SerieA-Team-League-Stats.csv', sep=';',
                                  encoding='latin-1')
    df_league_stats = df_league_stats.drop(
        ['MP', 'RkLeag', 'L', 'GD', 'Pts', 'xG', 'xGA', 'xGD', 'xGD/90', 'Attendance'],
        axis=1)
    df_defensive_actions = pd.read_csv('./data/SerieA-Team-Defensive-Actions.csv',
                                       sep=';', encoding='latin-1')
    df_defensive_actions = df_defensive_actions.drop(
        ['Def3rdTck', 'Mid3rdTck', 'Att3rdTck', 'TklWvsDrib', 'AttTckvsDrib',
         'TklWvsDribRt', 'PastDribNTck', 'PressRt', 'Def3rdPres', 'Mid3rdPres',
         'Att3rdPres', 'TotBlocBal', 'ShBlocBall', 'ShSvBloc', 'PassBlock',
         'TklpInt'], axis=1)
    df = pd.merge(df_standard_stats, df_shooting_stats, on="Squad")
    df = pd.merge(df, df_possession_stats, on="Squad")
    df = pd.merge(df, df_passing_stats, on="Squad")
    df = pd.merge(df, df_league_stats, on="Squad")
    df = pd.merge(df, df_defensive_actions, on="Squad")
    df.set_index("Squad")
    df.rename(columns=columns_names_dict, inplace=True)
    df.to_csv("./data/teams.csv")


# PLAYERS STATS
def clean_names(df):
    nomi = df['Player']
    nm = []
    index = []
    i = 0
    for nome in nomi:
        if "?" in nome or "\\" in nome:
            index.append(i)
            nm.append(nome)
        i = i + 1
    print(nm)
    fixed = ['Marko Arnautovic', 'Toma Basic', 'Filip Benkovic', 'Bartosz Bereszynski', 'Marcelo Brozovic',
             'Vlad Chiriches', 'Domen Crnigoj', 'Pawel Dawidowicz', 'Bartolmiej Dragowski', 'Radu Dragusin',
             'Radu Dragusin', 'Edin Dzeko', 'Albert Gudmundsson', 'Samir Handanovic', 'Zlatan Ibrahimovic', 'Ivan Ilic',
             'Josip Ilicic', 'Pawel Jaroszyski', 'Nikola Kalinic', 'Dimitrije Kamenovic', 'Rade Krunic',
             'Darko Lazovic', 'Sasa Lukic', 'Nikola Maksimovic', 'Razvan Marin', 'Adam Marusic', 'Alexa Matic',
             'Nikola Milenkovic', 'Sergej Milinkovic-Savic', 'Vanja Milinkovic-Savic', 'Matija Nastasic',
             'Mario Pasalic', 'Ivan Perisic', 'Krzysztof Piatek', 'Ivan Radovanovic', 'Ionut Radu', 'Stefan Radu',
             'Boris Radunovic', 'Ante Rebic', 'Arnór Sigursson', 'Lukasz Skorupski', 'Petar Stojanovic',
             'Wojciech Szczesny', 'Ciprian Tatarusanu', 'Aleksa Terzic', 'Dusan Vlahovic', 'Dusan Vlahovic',
             'Piotr Zieliski', 'Szymon Zurkowski', 'Milan curic', 'Filip Curic']
    j = 0
    for i in index:
        df.at[i, 'Player'] = fixed[j]
        j = j + 1


def import_players_stats():
    df_players = pd.read_csv('./data/2021-2022 Football Player Stats.csv', sep=';',
                             encoding='latin-1')
    df_players = df_players[df_players["Comp"] == "Serie A"]
    df_players = df_players.reset_index()
    df_players = df_players.drop(["Rk", "index"], axis=1)
    clean_names(df_players)
    df_players = df_players.loc[:,
                 ["Player", "Nation", "Pos", "Squad", "Age", "MP", "Min", "Goals", "Assists", "CrdY", "CrdR"]]
    df_players.rename(
        columns={"MP": "Match_Played", "Min": "Minutes", "CrdY": "Yellow_cards", "CrdR": "Red_Cards"}, inplace=True)
    df_players.to_csv("./data/players.csv")


# Main Method to call outside the file
def clean_data():
    import_squad_stats()
    import_players_stats()
