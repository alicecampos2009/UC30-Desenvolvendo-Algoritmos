# QUESTÃO 04

def academia(peso, altura):
    return peso * (altura * altura)

try:
    peso = float(input("Digete seu peso: "))
    altura = float(input("Digite sua altura: "))
    
    imc = academia(peso, altura)
    
    if imc <= 24.9:
        print("Magro")
    else:
        print(".")

except ValueError: 
    print("Erro capturado! Digite apenas números")
