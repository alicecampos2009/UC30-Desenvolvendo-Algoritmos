valorPassagem = float(input("Qual o valor da passagem?: "))
diasLetivos = int(input("Quantidade de dias letivos: ")) 

idaVolta = valorPassagem * 2
print("O valor gasto por dia é de: ", idaVolta)

valorTotal = idaVolta * diasLetivos
print("O valor que será gasto no final do ano é de: ", valorTotal)