import pandas as pd

data = pd.read_csv('data/churn.csv')

print(data.head())
print(data.columns)
print(data.info())
print("\n missing values")
print(data.isnull().sum())