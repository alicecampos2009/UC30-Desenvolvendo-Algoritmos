vendas = [120, 75, 200, 53, 84, 91, 150]

somaPares = 0

for valor in vendas:
    if valor % 2 == 0:
        somaPares += valor

print("Soma dos valores pares:", somaPares)