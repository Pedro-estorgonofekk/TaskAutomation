#Gerador de cartaz de procurado
#Libs: Path, pandas, time, pyautogui

from pathlib import Path
import pandas as pd
import pyautogui as pag
from time import sleep
from funcs.funcoes import AbrirNavegador, GerarCartaz, SalvarCartaz, UploadCartaz

#Importando planilha de procurados
procurados = pd.read_excel('procurados.xlsx')
dirExecucao = Path(__file__).resolve().parent


AbrirNavegador()
sleep(0.5)

#Loop pra iterar em cada linha da planilha e atribuir os dados

pag.alert("Gerando cartazes, pressione OK para continuar")
for i, row in procurados.iterrows():
    nome = row['Nome']
    crime = row['Crime']
    recompensa = row['Recompensa']

    GerarCartaz(nome, crime, recompensa, dirExecucao)
    sleep(0.5)
    UploadCartaz(dirExecucao, nome)

SalvarCartaz()
pag.alert("Automação concluída! Pressione OK para sair")