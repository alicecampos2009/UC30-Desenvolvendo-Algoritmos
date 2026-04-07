import random
numero = random.randint(1,100)

tentativas = int(input("Digite algum número e adivinhe-o de 1 a 100:"))

while tentativas != numero: 

    if tentativas == numero:
        print("Você acertou")
        break
    elif tentativas > numero:  
        print("Número digitado é maior")
    elif tentativas < numero:
        print("Número digitado é menor")