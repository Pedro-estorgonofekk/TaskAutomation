#1 Importar a biblioteca do pandas
import pandas as pd

#2 Carregar uma planilha do Excel
df = pd.read_excel('revisao/planilha.xlsx')
print(df.head())

#3 Inserir novos dados da Planilha
print(df.loc[0]) #imprime a primeira linha
print(df.loc[0, "Nome"]) #imprime a primeira linha
print(df.loc[0 : 3]) #vai ler a linha 0/linha inicial ate a 3/linha final
print(df.loc[4 : 5, "Nome"]) #Selecione a Coluna das linhas entre 4 e 5
print(df.loc[4 : 6, ["Nome", "Idade"]]) #Selecione a Coluna nomes e idade das linhas entre 4 a 6
print(df.loc[ : , "Nome"]) #Selecione uma unica coluna - todas as linhas

df2 = df.loc[3:6, ["Nome", "Sexo"]]
print(df2)

print(df2.loc[[True, False, False, True], ["Nome", "Sexo"]])

#3 Inserir novos dados da Planilha
df.loc[len(df)] = ["Isis", "Feminino", 18, "Tecnico em Informática", "Automação T", 10]
print(df)


#4 Atulizar dados na Planilha
df.loc[30,["Curso", "Disciplina"]] = ["Artes", "Teatro"]
print(df)

#5 Filtrar dados
condicao1 = df["Idade"] == 20
condicao2 = df["Sexo"] == 'Feminino'
print(df.loc[condicao1 & condicao2, "Nome"])

#6 Classificar Dados
tabela_ordenada = df.sort_values("Nome", ascending=True)
print(tabela_ordenada)

#7 Contar Dados
tabela_contagem = df.value_counts("Sexo")
print(tabela_contagem)

#8 Agrupar Dados
tabela_agrupada = df.groupby("Disciplina")["Nota"].sum() #Sum soma as notas, mean media e count 
print(tabela_agrupada)

#9 Exportar Dados
df.to_excel("revisao\\nova_planilha")