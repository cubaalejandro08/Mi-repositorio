saldo = 1000.0  # saldo inicial

while True:
    print("\n===== CAJERO =====")
    print("1. Consultar saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Salir")
    opcion = int(input("Elija una opción: "))

    match opcion:
        case 1:
            print(f"Su saldo es: {saldo:.2f}")
        case 2:
            monto = float(input("Monto a depositar: "))
            if monto > 0:
                saldo += monto
                print(f"Depósito exitoso. Nuevo saldo: {saldo:.2f}")
            else:
                print("El monto debe ser mayor que cero.")
        case 3:
            monto = float(input("Monto a retirar: "))
            if monto <= 0:
                print("El monto debe ser mayor que cero.")
            elif monto > saldo:
                print("Fondos insuficientes.")
            else:
                saldo -= monto
                print(f"Retiro exitoso. Nuevo saldo: {saldo:.2f}")
        case 4:
            print("Gracias por usar el cajero.")
        case _:
            print("Opción no válida.")

    if opcion == 4:
        break