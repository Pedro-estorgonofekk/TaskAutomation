import pyautogui as pag
from time import sleep

def blocoNotas(resposta):
    pag.hotkey("win", "d")
    pag.press("win")
    pag.write("bloco")
    sleep(0.5)
    pag.press("enter")
    sleep(0.5)
    pag.write(resposta)