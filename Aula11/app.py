import pandas as pd

planilha = pd.read_excel("./planilha.xlsx")

print(planilha.loc[1:9, "Nome"])
#print(planilha.head())