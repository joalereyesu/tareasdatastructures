import random

def CreateList(n):
    lista = []
    numbers = 0
    for x in range(0, n):
        #numbers += 1
        #lista.append(numbers)
        lista.append(random.randint(0,99))    
    lista.sort()
    return lista


def linearSearch(lista, value):
    if value in lista:
        return True
    else:
        False

def binarySearch(lista, l, r, value):
    while l <= r: 
  
        mid = l + (r - l) // 2; 

        if lista[mid] == value: 
            return True 
   
        elif lista[mid] < value: 
            l = mid + 1
  
        else: 
            r = mid - 1
    
    return False

