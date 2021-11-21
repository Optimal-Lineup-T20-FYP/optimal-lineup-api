import pandas as pd

batter = pd.read_csv('https://raw.githubusercontent.com/Optimal-Lineup-T20-FYP/Datasets/main/Batter_Statistics.csv')
bowler = pd.read_csv('https://raw.githubusercontent.com/Optimal-Lineup-T20-FYP/Datasets/main/Bowler_Statistics.csv')

batter.drop(['Unnamed: 0','NAME'], inplace=True, axis = 1)
bowler.drop(['Unnamed: 0','NAME'], inplace=True, axis = 1)

def getAllBattersName():
    return batter['Full name'].tolist()

def getAllBowlersName():
    return batter['Full name'].tolist()

def getPlayerData(player_name):
    batter_stats = None
    bowler_stats = None
    res = {}
    if player_name in batter['Full name'].values :
        batter_stats = batter[batter['Full name'] == player_name].drop('Full name',axis=1).to_dict('r')[0]
        res['batter'] = batter_stats
    if player_name in bowler['Full name'].values : 
        bowler_stats = bowler[bowler['Full name'] == player_name].drop('Full name',axis=1).to_dict('r')[0]
        res['bowler'] = bowler_stats
    return res