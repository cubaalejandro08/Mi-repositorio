
n = int(input("Ingrese la cantidad de números: "))
suma = 0

for i in range(n):
    num = int(input("Ingrese un número: "))
    suma += num

if n > 0:
    promedio = suma / n
    print("La suma es:", suma)
    print("El promedio es:", promedio)
else:
    print("No se puede calcular el promedio")
