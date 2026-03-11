salarioBase = (int("Seu salário é de 3500"))
bonus = (int("Você ganhou um bônus de 800"))
desconto = (int("Você recebe um desconto 250"))

print(salarioBase)
print(bonus)
print(desconto)

salarioBruto = salarioBase + bonus
print("Salário Bruto: ", salarioBruto)

salarioLiquido = salarioBruto - desconto
print("Salário Líquido: ", salarioLiquido) 