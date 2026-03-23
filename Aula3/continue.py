aluno1 = {"nome": "pablo", "idade": 17, "sexo": "M"}
aluno2 = {"nome": "Carlos", "idade": 18, "sexo": "M"}
aluno3 = {"nome": "Samara", "idade": 17, "sexo": "F"}

alunos = [aluno1, aluno2, aluno3]

for aluno in alunos:
    if aluno["idade"] >= 18:
        continue
    print(f"Olá {aluno["nome"]}, qual é o seu passa tempo? ")
    aluno["hobbie"] = input("")

print(alunos)