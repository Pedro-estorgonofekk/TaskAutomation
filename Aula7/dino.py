import pyautogui as pag
from time import sleep

pag.hotkey("win", "d")
pag.press("win")    
pag.write("chrome")

sleep(0.2)

pag.press("enter")

sleep(0.5)

pag.write("chrome://dino")
pag.press("enter")

sleep(0.5)
while True:
    pag.press("space")
    sleep(1)