"""
Print all prime numbers that exists between 100 to 1
Print them from largest number to smallest
Do not use loops (for, foreach, do, while)
Create your own method to define if a number is prime or not



def PrimeNum(n):
    if n < 100 :
        PrimeNum(n-1)
        print(n , end = ' ')

PrimeNum(100)



def es_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True   
   
   
print(*range(100,0,-1))

def es_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True    
    
def imprimir_y_verificar_primos(numero):
    if numero < 1:
        return
    else:
        if es_primo(numero):
            print(f"{numero} es primo")
        else:
            print(f"{numero} no es primo")
        imprimir_y_verificar_primos(numero - 1)
        
imprimir_y_verificar_primos(10)



    

# Definir una función lambda que devuelve los números del 100 al 1 en forma descendente
imprimir_descendente = lambda x: print(x)

# Utilizar la función map() para aplicar la función lambda a una secuencia descendente del 100 al 1
list(map(imprimir_descendente, range(100, 0, -1)))


#print(*range(100, 0, -1))

def prime (n):
    num_val = (*range(n, 0, -1))
    if num_val % 2 == 0 or num_val % 3 == 0:
        print(f"{n}es numero primo ")
    else:
        print(f"{n} no es numero primo ")
        
    
prime(100)
"""


def es_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def prime(n):
    if es_primo(n):
        print(f"{n} es número primo")
    else:
        print(f"{n} no es número primo")

print(*range(prime(100),0,-1))

