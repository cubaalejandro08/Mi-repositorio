import math

while True:
    print("\n===== ÁREAS DE FIGURAS =====")
    print("1. Cuadrado")
    print("2. Rectángulo")
    print("3. Triángulo")
    print("4. Círculo")
    print("5. Salir")
    opcion = int(input("Elija una opción: "))

    match opcion:
        case 1:
            lado = float(input("Lado: "))
            if lado > 0:
                print(f"Área del cuadrado: {lado * lado:.2f}")
            else:
                print("El lado debe ser mayor que cero.")
        case 2:
            base = float(input("Base: "))
            altura = float(input("Altura: "))
            if base > 0 and altura > 0:
                print(f"Área del rectángulo: {base * altura:.2f}")
            else:
                print("Las medidas deben ser mayores que cero.")
        case 3:
            base = float(input("Base: "))
            altura = float(input("Altura: "))
            if base > 0 and altura > 0:
                print(f"Área del triángulo: {base * altura / 2:.2f}")
            else:
                print("Las medidas deben ser mayores que cero.")
        case 4:
            radio = float(input("Radio: "))
            if radio > 0:
                print(f"Área del círculo: {math.pi * radio ** 2:.2f}")
            else:
                print("El radio debe ser mayor que cero.")
        case 5:
            print("Programa finalizado.")
        case _:
            print("Opción no válida.")

    if opcion == 5:
        break