def binary_search(lista, baixo, alto, item):
    # Caso base.
    if baixo <= alto:
        # Verifica o elemento central.
        meio = (baixo + alto) // 2
        # Acha o item.
        if lista[meio] == item:
            return meio
        # O item é menor que o elemento central, então ele está na sublista esquerda.
        elif lista[meio] > item:
            return binary_search(lista, baixo, meio - 1, item)
        # O item é maior que o elemento central, então ele está na sublista direita.
        else:
            return binary_search(lista, meio + 1, alto, item)
    # O item não está na lista.
    else:
        return -1


lista = [6, 7, 8, 9, 10]
print(binary_search(lista, 0, len(lista) - 1, 7))
print(binary_search(lista, 0, len(lista) - 1, 9))
