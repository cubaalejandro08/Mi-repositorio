suma = 0
cantidad = 0
mayor = None
menor = None

nota = float(input("Ingrese una nota (-1 para finalizar): "))

# "Mientras" -> while
while nota != -1:
    if 0 <= nota <= 100:
        suma += nota
        cantidad += 1
        if mayor is None or nota > mayor:
            mayor = nota
        if menor is None or nota < menor:
            menor = nota
    else:
        print("Nota no válida (debe estar entre 0 y 100).")

    nota = float(input("Ingrese una nota (-1 para finalizar): "))

if cantidad > 0:
    print(f"\nCantidad de notas: {cantidad}")
    print(f"Promedio: {suma / cantidad:.2f}")
    print(f"Nota mayor: {mayor}")
    print(f"Nota menor: {menor}")
else:
    print("No se ingresaron notas.")