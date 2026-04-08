N = int(input("Quantas pessoas foram infectadas inicialmente?: "))
R = int(input("Qual o fator reprodutivo?: "))
P = int(input("Quantas pessoas foram infectadas totalmente?: "))

infectadosDoDia = N
total = N
dias = 0

while total < P:
    novosInfectados = infectadosDoDia * R
    total += novosInfectados
    infectadosDia = novosInfectados
    dias += 1

print(dias) 