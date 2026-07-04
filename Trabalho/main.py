#Gerador de cartaz de procurado
#Libs: pandas, pyautogui, pillow

import pandas as pd
import pyautogui as pag
from time import sleep
from PIL import Image, ImageDraw, ImageFont


#Escolha de navegador
navegador = pag.prompt("Qual navegador você está usando? (chrome, edge, firefox)")

#Importando planilha de procurados
procurados = pd.read_excel('procurados.xlsx')

#Loop pra iterar sobre cada linha da planilha e atribuir os dados
for i, row in procurados.iterrows():
    nome = row['Nome']
    crime = row['Crime']
    recompensa = row['Recompensa']

    def CadastrarSuspeito(dado, navegador):
        #Abrindo navegador e acessando o link do formulário
        pag.hotkey("win", "d")
        pag.press("win")
        pag.write(navegador)
        sleep(1)
        
        pag.press("enter")
        sleep(2)

        pag.write("https://forms.gle/vngELUxv7hENFfyf7")
        pag.press("enter")
        sleep(2)

        #Localizando o campo de nome e preenchendo com o dado da planilha
        coords = pag.locateCenterOnScreen("imgs/pag/nome.png", confidence=0.9)
        pag.click(coords.x, coords.y + 30)
        pag.write(dado)

        

        
    def GerarCartaz(planilha):
        print(planilha)

    CadastrarSuspeito(procurados, navegador)

pag.alert("Cadastro concluído com sucesso!")