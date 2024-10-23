import pandas as pd

states = pd.read_csv('states.csv')

def display():
    for index, row in states.iterrows():
        name = row['name']
        lat = row['lat']
        lon = row['lon']
        print(name, lat, lon)

display()

