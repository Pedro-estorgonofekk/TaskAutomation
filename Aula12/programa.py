import pyautogui as pag
import pandas as pd
from time import sleep

pag.press("home")

def Preencher(imagem, deslocamentoY = 0, valor = None):
    campo = pag.locateCenterOnScreen(imagem,confidence=0.9)
    pag.click(campo.x, campo.y + deslocamentoY)
    if valor:
        pag.write(valor)
    pag.scroll(-150)
    sleep(1)

#Variaveis
nome = "Gustavo"
matricula = "2024190036"
curso = "INFO"
genero = "M"

Preencher("./imgs/email.png")
Preencher("./imgs/nome.png", 50, nome)
Preencher("./imgs/matricula.png", 50,matricula)
Preencher("./imgs/curso.png", 50,curso)
Preencher(f"./imgs/{genero}.png")
#Preencher("./imgs/enviar.png")


dados = pd.read_excel("./dados_automacao.xlsx")
for campo, linha in dados:
    print(linha)

