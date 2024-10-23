import pandas as pd

homes = pd.read_csv('homes.csv')

df = pd.DataFrame(homes)

df['size'] = [round(x) for x in df['size']]

df['price'] = [0 if x < 0 else x for x in df['price']]

df['year'] = [(x + 1900) if x < 100 else x for x in df['year']]

df['zipcode'] = [str(x)[0:5] if len(str(x)) > 5 else x for x in df['zipcode']]

def modern(df):
    if df.year >= 2012:
        return 'yes'
    else:
        return 'no'

df['modern'] = df.apply(modern, axis = 1)

def psf(df):
    return round(df.price/df['size'])

df['psf'] = df.apply(psf, axis = 1)


print(df)
