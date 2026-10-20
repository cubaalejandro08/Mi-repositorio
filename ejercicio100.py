while True:
    print("\n===== MENÚ =====")
    print("1. Factorial")
    print("2. Tabla de multiplicar")
    print("3. Paridad (par o impar)")
    print("4. Cuadrado")
    print("5. Salir")
    opcion = int(input("Elija una opción: "))

    match opcion:
        case 1:
            n = int(input("Ingrese un número: "))
            if n < 0:
                print("No existe factorial de números negativos.")
            else:
                factorial = 1
                for i in range(1, n + 1):
                    factorial *= i
                print(f"{n}! = {factorial}")
        case 2:
            n = int(input("Ingrese un número: "))
            for i in range(1, 11):
                print(f"{n} x {i} = {n * i}")
        case 3:
            n = int(input("Ingrese un número: "))
            if n % 2 == 0:
                print(f"{n} es PAR")
            else:
                print(f"{n} es IMPAR")
        case 4:
            n = float(input("Ingrese un número: "))
            print(f"El cuadrado de {n} es {n ** 2}")
        case 5:
            print("Programa finalizado.")
        case _:
            print("Opción no válida.")

    if opcion == 5:
        break
