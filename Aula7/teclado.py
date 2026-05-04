import pyautogui as pag
from funcoes.abrirTerm import abrirTerm
from funcoes.blocoNotas import blocoNotas
programa = pag.prompt("Programa de hj pae")

if programa == "termo":
    abrirTerm()
else:
    blocoNotas(programa)