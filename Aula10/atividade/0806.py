import pandas as pd

df_notas = pd.read_excel('./notas_estudantes.xlsx', sheet_name='Notas')
df_atividades = pd.read_excel('./notas_estudantes.xlsx', sheet_name='Atividades')

df_notas.loc[len(df_notas)] = {
    'Nome': 'Lucas Silva',
    'Atividade': 'Prova Final',
    'Nota': 8.5
}
df_notas.loc[df_notas.loc[(df_notas["Nome"] == "Ana Souza") & (df_notas["Atividade"] == "Trabalho 1")].index, ["Nota"]] = 9

df_notas.drop(df_notas.loc[(df_notas["Nome"] == "Pedro Santos") & (df_notas["Atividade"] == "Prova 1")].index, inplace=True)

df_notas = df_notas[df_notas['Nota'] > 7]

"""for i in (df_notas):
    df_notas = df_notas.groupby(i)
    print(i)"""

print(df_notas)