#!/usr/bin/env python3

def sumar(a, b): 
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "No se puede dividir por cero."
    else:
        return a / b
    
def potencia(a, b):
    return a**b

def factorial_recursivo(a):
    if a==0:
        return 1
    else:
        return a * factorial_recursivo(a-1)
    

def menu():
    print("Calculadora básica")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Pontecia")
    print("6. Factorial")
    print("7. Salir")

def main():
    while True:
        menu()
        opcion = input("Seleccione una opción (1/2/3/4/5/6/7): ")

        if opcion == '7':
            print("¡Hasta luego!")
            break
        elif opcion not in ['1', '2', '3', '4', '5', '6']:
            continue

        num1 = float(input("Ingrese el primer número: "))
    
        if opcion != '6':
            num2 = float(input("Ingrese el segundo número: "))

        if opcion == '1':
            print("Resultado:", sumar(num1, num2))
        elif opcion == '2':
            print("Resultado:", restar(num1, num2))
        elif opcion == '3':
            print("Resultado:", multiplicar(num1, num2))
        elif opcion == '4':
            print("Resultado:", dividir(num1, num2))
        elif opcion == '5':
            print("Resultado:", potencia(num1, num2))
        elif opcion == '6':
            print("Resultado:", factorial_recursivo(num1))
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
    