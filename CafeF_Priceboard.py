import pandas as pd
df = pd.read_json('http://banggia.cafef.vn/stockhandler.ashx?center=undefined')
df.to_csv("CafeF_Priceboard.csv")
print (df)
