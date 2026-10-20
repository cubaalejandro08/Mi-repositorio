ninos = 0
adolescentes = 0
adultos = 0
adultos_mayores = 0

n = int(input("¿Cuántas edades desea ingresar? "))

for i in range(1, n + 1):
    edad = int(input(f"Edad {i}: "))

    if edad < 0:
        print("Edad no válida, no se contará.")
    elif edad <= 11:
        ninos += 1
    elif edad <= 17:
        adolescentes += 1
    elif edad <= 59:
        adultos += 1
    else:
        adultos_mayores += 1

print("\n===== RESULTADOS =====")
print(f"Niños (0-11): {ninos}")
print(f"Adolescentes (12-17): {adolescentes}")
print(f"Adultos (18-59): {adultos}")
print(f"Adultos mayores (60+): {adultos_mayores}")