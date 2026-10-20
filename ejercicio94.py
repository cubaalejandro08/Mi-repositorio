mayores = 0
menores = 0

edad = int(input("Ingrese una edad (0 para terminar): "))

while edad != 0:
    if edad < 0:
        print("Edad no válida.")
    elif edad >= 18:
        mayores += 1
    else:
        menores += 1

    edad = int(input("Ingrese una edad (0 para terminar): "))

print(f"\nMayores de edad: {mayores}")
print(f"Menores de edad: {menores}")