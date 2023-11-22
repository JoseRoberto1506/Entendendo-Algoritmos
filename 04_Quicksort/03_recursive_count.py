def count(arr):
    # Caso base.
    if len(arr) == 1:
        return 1
    # Caso recursivo.
    else:
        return 1 + count(arr[1:])


print(count([1, 2, 3, 4, 5]))
