notaUm = float(input("Nota 1: "))
notaDois = float(input("Nota 2: "))
media = (notaUm + notaDois)/2

if media >= 6:
    print("Aporvado!")
else:
    exame = float(input("Exame final: "))
    media = (exame + media)/2
    
    if media > 6:
        print("Aporvado")
    else:
        print("Reporvado")