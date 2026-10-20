
n = int(input("Ingrese la cantidad de números: "))

positivos = 0
negativos = 0
ceros = 0

for i in range(n):
    num = int(input("Ingrese un número: "))

    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    else:
        ceros += 1

print("Cantidad de positivos:", positivos)
print("Cantidad de negativos:", negativos)
print("Cantidad de ceros:", ceros)
