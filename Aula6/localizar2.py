import pyautogui as pag

doisXy = pag.locateOnScreen('imagesLocations\\2.png', confidence=0.9, grayscale=False)
zeroXy = pag.locateOnScreen('imagesLocations\\0.png', confidence=0.9, grayscale=False)
maisXy = pag.locateOnScreen('imagesLocations\\+.png', confidence=0.9, grayscale=False)
seteXy = pag.locateOnScreen('imagesLocations\\7.png', confidence=0.9, grayscale=False)
igualXy = pag.locateOnScreen('imagesLocations\\=.png',confidence=0.9, grayscale=False)

for i in range(3):
    pag.click(doisXy, duration=0.2, interval=0.1)
    pag.click(zeroXy, duration=0.2, interval=0.1)
    pag.click(maisXy, duration=0.2, interval=0.1)

pag.click(seteXy, duration=0.2, interval=0.1)
pag.click(igualXy, duration=0.2, interval=0.1)
