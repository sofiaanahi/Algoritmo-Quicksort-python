def quicksort(array):
    # Si la lista tiene uno o cero elementos, ya esta ordenada
    if len(array) <= 1:
        return array
    
    # Elige el primer elemento como pivote
    pivot = array[0]

    # Sublista de elementos menores que el pivote
    left = [ x for x in array[1:] if x < pivot]

    # Sublista de elementos mayores o iguales al pivote
    right = [ x for x in array[1:] if x >= pivot]

    # Ordena recursivamente las sublistas y las combina con el pivote
    return quicksort(left) + [pivot] + quicksort(right)

# Pruebas para verificar el funcionamiento del algoritmo

# Prueba 1: Lista ordenada

print(quicksort([1,2,3,4,5,6,7,8,9,10]))   # debe devolver lo mismo

# Prueba 2: Lista desordenada 

print(quicksort([3,4,5,6,77,8,1,3,443,78,21]))   # debe devolver la lista ordenada

# Prueba 3: Lista con elementos repetidos

print(quicksort([1,1,1,2,2,3,5,3,53,5,5,6,7,7,7]))  #debe devolver la lista ordenada y sin repeticiones

# Prueba 4: Lista vacia
print(quicksort([]))   # debe devolver una lista vacia

# Prueba 5: Lista con un solo elemento
print(quicksort([33]))   # debe devolver el 33 