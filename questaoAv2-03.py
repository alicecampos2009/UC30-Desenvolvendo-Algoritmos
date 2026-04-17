total = 0

valor = float(input("Digite o valor do item ou digite 0 para encerrar: "))

while valor != 0:
    total += valor
    valor = float(input("Digite o valor do item ou digite 0 para encerrar: "))

print("Total da compra: R$", total)