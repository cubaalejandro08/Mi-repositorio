while True:
    numero = int(input("Ingrese un número: "))

    # "Para" -> for
    print(f"\nTabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

    respuesta = input("\n¿Desea ver otra tabla? (s/n): ").strip().lower()
    if respuesta != "s":
        break

print("Programa finalizado.")
