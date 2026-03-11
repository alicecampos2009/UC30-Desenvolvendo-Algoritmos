kmPercorrido = 450
consumo = 8
litroGasolina = 5.50

print("Quilômetros percorridos: ", kmPercorrido)
print("Consumo de gasolina em litros: ", consumo)
print("Valor do litro da gasolina: ", litroGasolina)

consumoLitro = kmPercorrido / consumo
custoTotal = consumoLitro * litroGasolina

print("A distância percorrida foi de ", kmPercorrido, "quilômetros.")
print("O consumo de gasolina foi de ", consumo, "litros.")
print("Foram consumidos", consumoLitro, "litros de gasolina.")
print("O valor do litro da gasolina foi de", custoTotal, "reais.")
