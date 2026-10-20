while True:
    print("\n===== CALCULADORA =====")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    opcion = int(input("Elija una opción: "))

    if opcion in (1, 2, 3, 4):
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))

    # "Según" -> match
    match opcion:
        case 1:
            print(f"Resultado: {a} + {b} = {a + b}")
        case 2:
            print(f"Resultado: {a} - {b} = {a - b}")
        case 3:
            print(f"Resultado: {a} x {b} = {a * b}")
        case 4:
            if b != 0:
                print(f"Resultado: {a} / {b} = {a / b}")
            else:
                print("Error: no se puede dividir entre cero.")
        case 5:
            print("Saliendo de la calculadora...")
        case _:
            print("Opción no válida.")

    if opcion == 5:
        break