def divisão(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("Não se divide por zero!")