from funcoes.exportDef import Escreva, Ler, PulaLinha, Soma

Escreva("Digite um numero: ")
numA = Ler()

PulaLinha()

Escreva("Digite oto numero: ")
numB = Ler()

PulaLinha()

Escreva(f"Soma: {Soma(numA, numB)}")