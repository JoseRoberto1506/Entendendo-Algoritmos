def max(arr):
    # Caso base.
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    # Caso recursivo.
    sub_max = max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max


print(max([2, 5, 4, 6, 1, 3]))
