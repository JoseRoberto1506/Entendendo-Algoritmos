def countdown(i):
    # Caso base.
    if i <= 0:
        return 0
    # Caso recursivo.
    else:
        print(i)
        return countdown(i - 1)


countdown(5)
