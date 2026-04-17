valor = float(input("Digite o valor da compra: "))

if valor > 500:
    desconto = valor * 0.20
elif valor >= 200:
    desconto = valor * 0.10
else:
    desconto = 0

precoFinal = valor - desconto

print("O valoor da sua compra foi de: ", precoFinal)