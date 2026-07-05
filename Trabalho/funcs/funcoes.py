import pyautogui as pag
from time import sleep
from PIL import Image, ImageDraw, ImageFont

def AbrirNavegador():
    pag.alert("Deixe o navegador em tela cheia")
    navegador = pag.prompt("Digite o navegador que deseja abrir").lower()

    array_navegadores = ['chrome', 'firefox', 'edge', 'opera', 'safari', 'brave', 'vivaldi', 'tor', 'chromium', 'opera gx']

    if navegador not in array_navegadores:
        pag.alert("Navegador não encontrado")
        return
    
    pag.hotkey("win", "d")
    sleep(0.1)
    pag.press("win")
    sleep(0.5)

    pag.write(navegador)
    sleep(0.5)
    pag.press("enter")
    sleep(2)

def SalvarCartaz():
    try:
        coords = pag.locateOnScreen("assets/pag/criar.png", confidence=0.8)
    except:
        pag.alert("Não foi possivel localizar o botão de criar")
        return

    pag.click(coords)
    sleep(2)

    #n esquece de alterar isso aq
    pag.write("8===D", interval=0.1)
    sleep(0.5)

    try:
        coords = pag.locateOnScreen("assets/pag/arquivo.png", confidence=0.8)
    except:
        pag.alert("Não foi possível localizar o botão de arquivo")
        pag.press("esc")
        
    
    pag.click(coords)
    sleep(0.5)

    try:
        coords = pag.locateOnScreen("assets/pag/baixar.png", confidence=0.8)
    except:
        pag.alert("Não foi possível localizar o botão de baixar")
        return

    pag.moveTo(coords)
    sleep(0.5)

    try:
        coords = pag.locateOnScreen("assets/pag/pdf.png", confidence=0.8)
    except:
        pag.alert("Não foi possível localizar o botão de baixar PDF")
        return

    pag.click(coords)
    sleep(0.5)

def Centralizado(draw, img, texto, y, fonte, cor="white"):
    bbox = draw.textbbox((0, 0), texto, font=fonte)
    largura = bbox[2] - bbox[0]

    x = (img.width - largura) / 2

    draw.text((x, y), texto, fill=cor, font=fonte)

def GerarCartaz(nome, crime, recompensa):
    #tratamento de erro float is not a string
    nome = str(nome)
    crime = str(crime)
    recompensa = str(recompensa)

    img = Image.open("assets/pill/modelo.png")
    draw = ImageDraw.Draw(img)

    fontNome = ImageFont.truetype("assets/font/Anton-Regular.ttf", 80)
    fontCrime = ImageFont.truetype("assets/font/Anton-Regular.ttf", 40)
    fontRecompensa = ImageFont.truetype("assets/font/Anton-Regular.ttf", 60)

    #Escreve o nome e o crime na imagem
    Centralizado(draw, img, nome, 400, fontNome, "white")
    Centralizado(draw, img, crime, 600, fontCrime, "white")
    Centralizado(draw, img, recompensa, 800, fontRecompensa, "white")

    img.show()


"""
#Fazer q ele consiga digitar o local do arquivo q vai ser subido ao google docs
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

botao = BASE_DIR / "imagens" / "botao.png"
login = BASE_DIR / "imagens" / "login.png"
planilha = BASE_DIR / "dados" / "clientes.xlsx"

print(botao)
"""