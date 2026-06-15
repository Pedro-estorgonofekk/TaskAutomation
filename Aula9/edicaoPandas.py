import pandas as pd

planilha = pd.read_excel("./Planilha/Dados.xlsx")

planilha.loc[16] = ['Pablo', 52, 1.8, 'Masculino']

planilha.loc[16] = ['Pablo', 52, 1.8, 'Masculino']
print(planilha)