def busca_menor(arr):
    # Armazena o menor valor.
    menor = arr[0]
    # Armazena o índice do menor valor.
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice


def ordenacao_por_selecao(arr):
    novo_arr = []
    for i in range(len(arr)):
        # Encontra o menor elemento do array e adiciona ao novo array.
        menor = busca_menor(arr)
        novo_arr.append(arr.pop(menor))
    return novo_arr


print(ordenacao_por_selecao([5, 3, 6, 2, 10]))
