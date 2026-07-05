import pyautogui as pag
from time import sleep
from PIL import Image, ImageDraw, ImageFont

def AbrirNavegador():
    navegador = pag.prompt("Digite o navegador que deseja abrir").lower()

    array_navegadores = ['chrome', 'firefox', 'edge', 'opera', 'safari', 'brave', 'vivaldi', 'tor', 'chromium', 'opera gx']

    if navegador not in array_navegadores:
        pag.alert("Navegador não encontrado")
        return
    
    pag.hotkey("win", "d")
    sleep(0.1)
    pag.press("win")
    sleep(1)

    pag.write(navegador)
    sleep(1)
    pag.press("enter")
    sleep(2)
    pag.hotkey("alt", "space")
    pag.press("x")
    sleep(1)

    pag.write("https://docs.google.com")
    pag.press("enter")
    sleep(2)

    try:
        coords = pag.locateCenterOnScreen("assets/pag/criar.png", confidence=0.8)
    except:
        pag.alert("Não foi possivel localizar o botão de criar")
        return

    pag.click(coords)
    sleep(2)

def UploadCartaz(dirExecucao, nome):
    try:
        coords = pag.locateCenterOnScreen("assets/pag/inserir.png", confidence=0.8)
    except:
        pag.alert("Não foi possível localizar o botão de inserir")
        return
    
    pag.click(coords)
    sleep(1)

    try:
        coords = pag.locateCenterOnScreen("assets/pag/imagem.png", confidence=0.8)
    except:
        pag.alert("Não foi possível localizar o botão de adicionar imagem")
        return
    
    pag.moveTo(coords)
    sleep(1)

    try:
        coords = pag.locateCenterOnScreen("assets/pag/upload.png", confidence=0.6)
        print(coords)
    except:
        pag.alert("Não foi possível localizar o botão de upload")
        return
        
    pag.click(coords)
    sleep(1)

    pag.write(str(dirExecucao / "assets" / "pill" / f"{nome}.png"), interval=0.01)
    pag.press("enter")
    sleep(1)


def SalvarCartaz():
    try:
        coords = pag.locateCenterOnScreen("assets/pag/arquivo.png", confidence=0.8)
    except:
        pag.alert("Não foi possível localizar o botão de arquivo")
        return
        
    pag.click(coords)
    sleep(1)

    try:
        coords = pag.locateCenterOnScreen("assets/pag/baixar.png", confidence=0.8)
    except:
        pag.alert("Não foi possível localizar o botão de baixar")
        return

    pag.moveTo(coords)
    sleep(1)

    try:
        coords = pag.locateCenterOnScreen("assets/pag/pdf.png", confidence=0.8)
    except:
        pag.alert("Não foi possível localizar o botão de baixar PDF")
        return

    pag.click(coords)
    sleep(1)

def Centralizado(draw, img, texto, y, fonte, cor="white"):
    bbox = draw.textbbox((0, 0), texto, font=fonte)
    largura = bbox[2] - bbox[0]

    x = (img.width - largura) / 2

    draw.text((x, y), texto, fill=cor, font=fonte)

def GerarCartaz(nome, crime, recompensa, dirExecucao):


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
    Centralizado(draw, img, nome, 200, fontNome, "white")
    Centralizado(draw, img, crime, 600, fontCrime, "white")
    Centralizado(draw, img, f"Recompensa: R${recompensa}", 700, fontRecompensa, "white")

    img.save(f"{dirExecucao}/assets/pill/{nome}.png", "PNG")



"""
#Fazer q ele consiga digitar o local do arquivo q vai ser subido ao google docs
from pathlib import Path

botao = BASE_DIR / "imagens" / "botao.png"
login = BASE_DIR / "imagens" / "login.png"
planilha = BASE_DIR / "dados" / "clientes.xlsx"

print(botao)
"""