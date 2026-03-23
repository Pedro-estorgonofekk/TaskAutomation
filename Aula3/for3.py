#Comando break: Interrompe o laço de repetição

nomes = ["Lucas", "Jesuely", "Caua", "Filipe"]

nomeRandom = ""

for nome in nomes:
    if nome.startswith("C"):
        nomeRandom = nome 
        break

print(f"O primeiro nome iniciado com C é {nomeRandom}")