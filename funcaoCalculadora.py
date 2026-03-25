valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite outro valor: "))
print(valor1, "e", valor2)

print("Qual operação você deseja fazer?: ")

print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
print("5. Sair")

operacao = input("Escolha sua opção: ")

if operacao == "1":
    print("A soma dos dois números é de: ", valor1 + valor2)

elif operacao == "2":
    print("A subtração dos dois números é de: ", valor1 - valor2)

elif operacao == "3":
    print("A multiplicação dos dois números é de: ", valor1 * valor2)

elif operacao == "4":
    print("A divisão dos dois números é de: ", valor1 / valor2) 

elif operacao == "5":
    print("Fechado programa...") 

else:
    print("Essa opção não existe!") 