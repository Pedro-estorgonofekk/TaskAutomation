import pandas as pd

planilha = pd.read_excel('pranias\\Alunos.xlsx')

planilha.loc[5, ["Nome", "Idade"]]
planilha.loc[5, ["Nome", "Idade"]] = ["Ronaldo", 18]

planilha.loc[len(planilha), ["Nome", "Idade", "Gênero"]] = ["Pedro", 17, "M"]
print(planilha)