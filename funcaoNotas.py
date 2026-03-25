def notasAlunos():
    print("Resumo Estatístico")

av1 = float(input("Digite sua nota da AV1: "))
av2 = float(input("Digite sua nota da AV2: "))
av3 = float(input("Digite sua nota da AV3: "))

soma = av1 + av2 + av3
média = soma / 3
maiorNota = max(av1, av2, av3)
menorNota = min(av1, av2, av3)

print("Seu relatório escolar: ") 

print("A soma das suas notas é de: ", soma)
print("A sua média é de: ", média)
print("A sua maior nota foi: ", maiorNota)
print("A sua menor nota foi: ", menorNota )