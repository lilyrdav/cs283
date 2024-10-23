import pandas as pd

states = pd.read_csv('states.csv')

def dist(lat1, lon1, lat2, lon2):
    return ((lat1 - lat2)**2 + (lon1 - lon2)**2)**(1/2)


def closest(lat, lon):
    min = 100
    minState = ''
    for index, row in states.iterrows() :
        value = dist(lat, lon, row['lat'], row['lon'])
        if value < min:
            min = value
            minState = row['name']
    return minState

print(closest(44.6,-89.8))
print(closest(42,-73))
print(closest(40.7,-77))