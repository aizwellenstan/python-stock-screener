import pandas as pd

df = pd.read_csv (r'./csv/sector.csv', index_col=0)
df.drop
sectorLst = df.groupby('sector')['symbol'].apply(list)
print(sectorLst)