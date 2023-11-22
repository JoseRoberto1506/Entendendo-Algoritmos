def quicksort(array):
    # Caso base. Arrays com 0 ou 1 elementos já estão "ordenados".
    if len(array) < 2:
        return array
    else:
        # Caso recursivo.
        pivo = array[0]
        # Subarray de todos os elementos menores do que o pivô.
        menores = [i for i in array[1:] if i <= pivo]
        # Subarray de todos os elementos maiores do que o pivô.
        maiores = [i for i in array[1:] if i > pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)


print(quicksort([10, 5, 2, 3]))
