import pandas as pd

flu = pd.read_csv('flu_tweets.csv')

def display():
    for index, row in flu.iterrows():
        name = row['name']
        lat = row['lat']
        lon = row['lon']
        print(name, lat, lon)

display()

