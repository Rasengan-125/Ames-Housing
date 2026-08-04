import pandas as pd

df_check = pd.read_csv("./data/train_cleaned.csv")
print(df_check.isnull().sum().sum())
