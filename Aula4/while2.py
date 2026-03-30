cont = True

while cont:
    aluno = input("Digite o nome do aluno: ")

    resp = int(input("Deseja continuar:\n0 - não\n1 - Sim\n:"))

    if resp == 0:
        cont = False
    elif resp == 1:
        cont = True
    else:
        while True:
            print("digitou errado bobalhão")

            