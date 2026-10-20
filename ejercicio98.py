aprobadas = 0
reprobadas = 0
suma = 0
mayor = 0
menor = 100

for i in range(1, 11):
    nota = float(input(f"Ingrese la nota {i}: "))
    while nota < 0 or nota > 100:
        nota = float(input("Nota no válida. Ingrese entre 0 y 100: "))

    suma += nota

    if nota >= 51:
        aprobadas += 1
        print("  -> Aprobada")
    else:
        reprobadas += 1
        print("  -> Reprobada")

    if nota > mayor:
        mayor = nota
    if nota < menor:
        menor = nota

print("\n===== ESTADÍSTICAS =====")
print(f"Aprobadas: {aprobadas}")
print(f"Reprobadas: {reprobadas}")
print(f"Promedio: {suma / 10:.2f}")
print(f"Nota mayor: {mayor}")
print(f"Nota menor: {menor}")
print(f"Porcentaje de aprobación: {aprobadas * 10}%")