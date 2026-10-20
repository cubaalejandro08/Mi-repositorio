
for i in range(10):
    num = int(input("Ingrese un número: "))

    if i == 0:
        mayor = num
        menor = num

    if num > mayor:
        mayor = num

    if num < menor:
        menor = num

print("El número mayor es:", mayor)
print("El número menor es:", menor)
