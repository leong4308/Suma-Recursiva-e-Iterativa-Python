
def suma_iterativa(n):
    suma = 0
    while n > 0:
        suma += n % 10
        n = n // 10
    return suma

def suma_recursiva(n):
    if n <= 9:
        return n
    else:
        return suma_recursiva(n // 10) + n % 10

def main():
    try:
        numero = int(input("Ingrese un número entero: "))
        resultado_iterativo = suma_iterativa(numero)
        resultado_recursivo = suma_recursiva(numero)

        print("Suma iterativa de los dígitos:", resultado_iterativo)
        print("Suma recursiva de los dígitos:", resultado_recursivo)

    except ValueError:
        print("Entrada no válida. Ingrese un número entero.")

    input("Presione Enter para salir.")

if __name__ == "__main__":
    main()
