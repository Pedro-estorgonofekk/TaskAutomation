import pyautogui as pag
from funcoes.abrirTerm import abrirTerm
from funcoes.blocoNotas import blocoNotas

pag.hotkey("win", "d")
programa = pag.prompt("Programa de hj pae")

if programa == "termo":
    abrirTerm()
elif programa == "rola":
    blocoNotas("8====D")
else:
    blocoNotas(programa)