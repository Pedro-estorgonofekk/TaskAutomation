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

    pag.write("https://docs.google.com")
    pag.press("enter")
    sleep(2)

    try:
        coords = pag.locateOnScreen("imgs/pag/criar.png", confidence=0.8)
    except:
        pag.alert("Não foi possivel localizar o botão de criar")
        return

    pag.click(coords)
    sleep(2)

    #n esquece de alterar isso aq
    pag.write("8===D", interval=0.1)

    try:
        coords = pag.locateOnScreen("imgs/pag/arquivo.png", confidence=0.8)
    except:
        pag.alert("Não foi possível localizar o botão de arquivo")
        pag.press("esc")
        
    
    pag.click(coords)

    try:
        coords = pag.locateOnScreen("imgs/pag/baixar.png", confidence=0.8)
    except:
        pag.alert("Não foi possível localizar o botão de baixar")
        return

    pag.moveRel(coords)

def GerarCartaz(nome, crime, recompensa):
    print(f"Nome: {nome}, Crime: {crime}, Recompensa: {recompensa}")
