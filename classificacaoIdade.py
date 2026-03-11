idade = int(input("Digite sua idade para saber qual a sua categoria!: "))

if idade < 12:
    categoria = "Categoria infantil"
elif idade < 18:
    categoria = "Categoria juveil"
elif idade < 60:
    categoria = "Categoria adulto"
else:
    categoria = "Categoria sênior"

print("Sua categoria é: ", categoria)