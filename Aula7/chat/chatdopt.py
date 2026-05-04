import pyautogui
from time import sleep

pergunta = pyautogui.prompt("O que deseja saber hoje?")

pyautogui.hotkey("win", "d")
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

sleep(2)

pyautogui.hotkey('win', 'up')

pyautogui.write('http://www.chatgpt.com')
pyautogui.press('enter')

sleep(3)

pyautogui.write(pergunta)
pyautogui.press('enter')


while True:
    pyautogui.scroll(-100)
    try:
        xy = pyautogui.locateCenterOnScreen('img\\copiar.png', confidence=.98)
        break
    except:
        pyautogui.scroll(-100)


sleep(2)

pyautogui.click(xy)

sleep(2)

pyautogui.hotkey("win", "d")
pyautogui.press("win")

pyautogui.write("bloco")
sleep(0.5)

pyautogui.press("enter")
sleep(0.5)

pyautogui.hotkey("ctrl", "v")