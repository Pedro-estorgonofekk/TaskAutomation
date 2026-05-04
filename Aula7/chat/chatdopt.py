import pyautogui
from time import sleep

#abre uma janela de entrada de dados
pergunta = pyautogui.prompt("O que deseja saber hoje?")

#pressiona um atalho do teclado 
#(win + d minimiza janelas e mostra desktop)
pyautogui.hotkey("win", "d")
#pressiona a tecla win
pyautogui.press('win')
#digita um texto onde o curso está
pyautogui.write('chrome')
#pressiona a tecla enter
pyautogui.press('enter')

#faz uma pausa de 2 segundos
sleep(2)

#maximiza a janela do chrome
pyautogui.hotkey('win', 'up')

#digita um endereço na url
pyautogui.write('http://www.chatgpt.com')
pyautogui.press('enter')

#faz uma pausa
sleep(3)

#digita o texto armazenado na variavel pergunta
pyautogui.write(pergunta)
pyautogui.press('enter')


while True:
    pyautogui.scroll(-100)
    try:
        xy = pyautogui.locateCenterOnScreen('img\\copiar.png', confidence=.98)
        break
    except:
        pyautogui.scroll(-100)


#faz uma pausa
sleep(2)

#localiza a coordenadas na imagem na tela
#clica na imagem
pyautogui.click(xy)

#faz uma pausa
sleep(2)

pyautogui.hotkey("win", "d")
pyautogui.press("win")

pyautogui.write("bloco")
sleep(0.5)

pyautogui.press("enter")
sleep(0.5)

pyautogui.hotkey("ctrl", "v")