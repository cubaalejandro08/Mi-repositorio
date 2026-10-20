pares = 0
impares = 0
positivos = 0
negativos = 0

numero = int(input("Ingrese un número (0 para terminar): "))

while numero != 0:
    # Operador módulo (%) para paridad
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    # Operadores relacionales para el signo
    if numero > 0:
        positivos += 1
    else:
        negativos += 1

    numero = int(input("Ingrese un número (0 para terminar): "))

print(f"\nPares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")