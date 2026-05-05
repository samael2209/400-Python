# Escribe una función que tome una lista de tuplas
# y las ordene en función del segundo elemento de cada tupla.

t = [(1, 5), (2, 3), (4, 1), (0, 9)]


def partition(arr, low, high):
    pivote = arr[high][1]
    
    i = low - 1
    
    for j in range(low, high):
        if arr[j][1] <= pivote:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[high] = arr[high], arr[i + 1]
    
    return i + 1
    

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

quicksort(t, 0, len(t) - 1)
print(t)

