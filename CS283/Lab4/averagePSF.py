import pandas as pd
from home import Home

homes = pd.read_csv('homes.csv')

list = []

for index, row in homes.iterrows() :
    if row['price'] > 0 and row['year'] > 1900 and row['size'] > 0:
        list.append(Home(row['zipcode'], row['price'], row['year'], row['size']))

for obj in list:
    print(obj.zip, obj.price, obj.year, obj.size)

sum = 0
count = 0
for h in list:
    sum += h.psf()
    count += 1

print(round(sum/count))


