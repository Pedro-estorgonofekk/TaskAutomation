##Precisa da Calculadora aberta do windows 1920x1080

import pyautogui as pag
from time import sleep

sleep(1)

for i in range (3):
    pag.click(170,485, duration=0.5, interval=0.1)
    pag.click(170,535, duration=0.5, interval=0.1)
    pag.click(335,483, duration=0.5, interval=0.1)

pag.click(90, 373, duration=0.5, interval=0.1)
pag.click(324, 525, duration=0.5, interval=0.1)