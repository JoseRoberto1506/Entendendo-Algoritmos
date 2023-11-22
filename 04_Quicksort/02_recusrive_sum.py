def sum(arr):
    # Caso base.
    if arr == []:
        return 0
    # Caso recursivo.
    else:
        return arr[0] + sum(arr[1:])


print(sum([1, 2, 3, 4]))
