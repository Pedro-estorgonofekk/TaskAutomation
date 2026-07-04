#Gerador de cartaz de procurado
#Libs: pandas, pyautogui, pillow e uma importação de funções do arquivo funcoes.py

import pandas as pd
import pyautogui as pag
from time import sleep
from PIL import Image, ImageDraw, ImageFont
from funcs.funcoes import AbrirNavegador, GerarCartaz

#Importando planilha de procurados
procurados = pd.read_excel('procurados.xlsx')

AbrirNavegador()

#Loop pra iterar em cada linha da planilha e atribuir os dados
for i, row in procurados.iterrows():
    nome = row['Nome']
    crime = row['Crime']
    recompensa = row['Recompensa']

    GerarCartaz(nome, crime, recompensa)