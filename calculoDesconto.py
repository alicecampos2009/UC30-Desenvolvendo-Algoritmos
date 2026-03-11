valorCompra = float(input("Digite o valor da sua compra: "))

if valorCompra < 100:
    desconto = 0
elif valorCompra < 500:
    desconto = valorCompra * 0.05
elif valorCompra < 1000: 
    desconto = valorCompra * 0.15

valorFinal = valorCompra - desconto

print("O valor da compra foi de:", valorCompra)
print("O valor do desconto foi de:", desconto)
print("O total a pagar é de:", valorFinal)