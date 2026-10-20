total = 0  # acumulador
cantidad_productos = 0

while True:
    print("\n===== REGISTRO DE PRODUCTOS =====")
    print("1. Agregar producto")
    print("2. Finalizar")
    opcion = int(input("Elija una opción: "))

    match opcion:
        case 1:
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
            subtotal = precio * cantidad
            total += subtotal  # acumulador
            cantidad_productos += 1
            print(f"{nombre} agregado. Subtotal: {subtotal:.2f}")
        case 2:
            print(f"\nProductos registrados: {cantidad_productos}")
            print(f"TOTAL A PAGAR: {total:.2f}")
        case _:
            print("Opción no válida.")

    if opcion == 2:
        break