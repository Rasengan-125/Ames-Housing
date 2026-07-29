import pandas as pd

df = pd.read_csv("train.csv")


print(df.groupby("MasVnrType")["MasVnrArea"].mean())
print()
# print(df.groupby("MasVnrType")["SalePrice"].mean())
print(df["MasVnrArea"].corr(df["SalePrice"]))
