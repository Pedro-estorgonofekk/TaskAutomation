import pyautogui as pag
from time import sleep

def abrirTerm():
    pag.hotkey("win", "d")
    pag.press("win")
    pag.write("chrome")
    pag.press("enter")

    sleep(0.5)
    pag.hotkey("ctrl", "shift", "n")

    sleep(0.15)
    pag.write("term.ooo")
    pag.press("enter")

    sleep(1.5)
    pag.write("raios")
    pag.press("enter")

    sleep(1.5)
    pag.write("funde")
    pag.press("enter")

    sleep(0.15)
    pag.click([200, 200])
    