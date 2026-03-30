user = input("Usuário: ")
password = input("Senha: ")

while user != "admin" or password != "admin123":
    user = input("Usuário: ")
    password = input("Senha: ")

print("Bem vindo administrador")