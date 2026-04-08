numeroPao = int(input("Quantos pães foram vendidos essa semana? "))
numeroDoce = int(input("Quantos doces foram vendidos essa semana? "))
numeroBolo = int(input("Quantos bolos foram vendidos essa semana? "))

soma = (numeroPao * 1) + (numeroDoce * 2) + (numeroBolo * 3)

if soma >= 150:
    print("B")
elif soma >= 120:
    print("D")
elif soma >= 100:
    print("P")
else:
    print("N") 