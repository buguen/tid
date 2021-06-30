import pandas as pd
url = 'https://raw.githubusercontent.com/buguen/tid/master/tag_model.csv'
df = pd.read_csv(url,index_col='num')
tag = df.loc['0x1170']

