import json
import pandas as pd

with open('./screener.json') as f:
    df = json.load(f)
df = df['data']

symbolLst = []
for i in df:
  symbol = i['d'][1]
  symbolLst.append(symbol)

df = pd.DataFrame(symbolLst)
df.columns = ['symbol']
df.to_csv('./symbolLst.csv')