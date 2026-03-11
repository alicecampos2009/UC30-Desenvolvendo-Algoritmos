aluno = {}

aluno["nome"] = input("Qual o seu nome?: ")
aluno["nota1"] = float(input("Qual foi sua nota na 1ª prova?: "))
aluno["nota2"] = float(input("Qual foi sua nota na 2ª prova?: "))

media = (aluno["nota1"] + aluno["nota2"]) / 2

aluno["media"] = media

print("\n Relatório:")
print("Nome:", aluno["nome"])
print("1ª nota:", aluno["nota1"])
print("2ª nota:", aluno["nota2"])
print("Média:", aluno["media"])

if media >= 7:
    print("Situação: Aprovado!")
elif media >= 5:
    print("Situação: Recuperação!")
else:
    print("Situação: Reprovado!") 