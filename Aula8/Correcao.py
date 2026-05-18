import pyautogui as pag
from time import sleep


## Area de trabalho
pag.hotkey("win", "d")

#Input
cpf = pag.prompt("Digite o CPF sem simbolos")

## Abre o ngc do windows
pag.press("win")
sleep(1)

## Digita paint
pag.write("Paint")
sleep(1)

## Abre o Paint
pag.press("enter")
sleep(1)

##Verifica a tela cheia
try:
    pag.locateOnScreen("imgs\\telaCheia.png", confidence=0.8)
    print("ja ta tela cheia")
except:
    ## Tela cheia
    pag.hotkey("win", "up")

largura, altura = pag.center([0, 0, 1920, 1080])

pag.moveTo(largura, altura)


##Desenho part 1
pag.dragRel(0, 100, 0.4)
pag.dragRel(300, 0, 0.4)
pag.dragRel(0, -200, 0.4)
pag.dragRel(-250, 0, 0.4)
pag.dragRel(50, 100, 0.4)
pag.dragRel(0, 100, 0.4)

##Desenho Part 2
pag.moveRel(-50, -200)
pag.dragRel(-50, 100, 0.4)
pag.dragRel(100, 0, 0.4)
pag.dragRel(200, 0, 0.4)

baldeXy = pag.locateOnScreen("imgs\\balde.png", confidence=0.8)
pag.click(baldeXy, duration=0.2, interval=0.1)

## Pintar telhado
marromXy = pag.locateOnScreen("imgs\\marrom2.png", confidence=0.98, grayscale=False)
pag.click(marromXy, duration=0.2, interval=0.1)

pag.moveTo(largura, altura)
pag.moveRel(24, -24)
pag.doubleClick()

pag.moveRel(100,0)
pag.doubleClick()

## Pintar parede
amareloXy = pag.locateOnScreen("imgs\\amarelo.png", confidence=0.999, grayscale=False)
pag.click(amareloXy, duration=0.2, interval=0.1)

pag.moveTo(largura, altura)
pag.moveRel(40, altura-240)
pag.doubleClick()

pag.moveRel(0,100)
pag.doubleClick()

pag.hotkey("ctrl", "s")
sleep(1)

pag.write(rf"C:\Users\{cpf}\Desktop")
