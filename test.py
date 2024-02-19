def es_primo(numero):
    if numero <= 1:
        return False  # Los números menores o iguales a 1 no son primos
    elif numero <= 3:
        return True   # 2 y 3 son primos

    # Verificar si el número es divisible por 2 o 3
    if numero % 2 == 0 or numero % 3 == 0:
        return False  # Si es divisible por 2 o 3, no es primo

    # Verificar los números de la forma 6k +/- 1 hasta la raíz cuadrada del número
    maximo = int(numero ** 0.5) + 1
    k_values = range(5, maximo, 6)
    return all(numero % k == 0 and numero % (k + 2) == 0 for k in k_values)

# Ejemplo de uso:
numero = int(input("Ingrese un número para verificar si es primo: "))

if es_primo(numero):
    print(f"{numero} es primo")
else:
    print(f"{numero} no es primo")
    

    