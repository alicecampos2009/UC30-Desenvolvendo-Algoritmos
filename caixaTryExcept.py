def caixaMercado(produto1, produto2):
    return produto1 + produto2

try:
    produto1 = float(input("Digite o preço do produto 1: "))
    produto2 = float(input("Digite o preço do produto 2: "))

    resultado = caixaMercado(produto1, produto2)
    print("O valor total é de: ", resultado)

except ValueError:
    print("Erro capturado! Digite apenas números")