def soma_segura(a, b):
    try:
        return a + b
    except TypeError:
        print("Entrada inválida! Digite somente números")
        return 0