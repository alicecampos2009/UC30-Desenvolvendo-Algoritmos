notas = [8.5, 6.0, 7.2, 9.0, 5.5, 7.8, 6.9]

quantidade = 0

for nota in notas:
    if nota > 7:
        quantidade += 1

print("Quantidade de notas acima de 7:", quantidade)