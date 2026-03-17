#inputs
nome = input("Nome: ")
idade = int(input("Idade: "))

if idade < 18:
    autorizacao = input("Pode? Sim ou não: ").lower()

    if autorizacao == "não" or autorizacao == "nao":
        print("Não pode!")

print(f"realizando embarque de {nome}")