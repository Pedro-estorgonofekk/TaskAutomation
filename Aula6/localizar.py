import pyautogui as pag

doisXy = pag.locateOnScreen('imagesLocations\\2.png', confidence=0.9)
zeroXy = pag.locateOnScreen('imagesLocations\\0.png', confidence=0.9)
maisXy = pag.locateOnScreen('imagesLocations\\+.png', confidence=0.9)
seteXy = pag.locateOnScreen('imagesLocations\\7.png', confidence=0.9)
igualXy = pag.locateOnScreen('imagesLocations\\=.png',confidence=0.9)

for i in range(3):
    pag.click(doisXy, duration=0.2, interval=0.1)
    pag.click(zeroXy, duration=0.2, interval=0.1)
    pag.click(maisXy, duration=0.2, interval=0.1)

pag.click(seteXy, duration=0.2, interval=0.1)
pag.click(igualXy, duration=0.2, interval=0.1)
