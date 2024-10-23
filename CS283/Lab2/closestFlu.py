from ast import increment_lineno
import pandas as pd

flu = pd.read_csv('flu_tweets.csv')
states = pd.read_csv('states.csv')

def dist(lat1, lon1, lat2, lon2):
    return ((lat1 - lat2)**2 + (lon1 - lon2)**2)**(1/2)


def closest(lat, lon):
    min = 100000000
    minState = ''
    for index, row in states.iterrows() :
        value = dist(lat, lon, row['lat'], row['lon'])
        if value < min:
            min = value
            minState = row['name']
    return minState

count = {}
def countTweets() :
    for index, row in flu.iterrows():
        clst = closest(row['lat'], row['lon'])
        # print(clst)
        # print(clst, ":", row['text'])
        if clst in count :
            count[clst] = count[clst] + 1
        else :
            count[clst] = 1
    for key in count.keys() :
        print (key, ":", count[key])
        
countTweets()