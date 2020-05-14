import pandas as pd

df=pd.read_csv('train.csv',nrows=100)
print('Files present=',df)

print(df.value_counts)
