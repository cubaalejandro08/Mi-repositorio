class Nodo:
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, codigo, descripcion):
        nuevo = Nodo(codigo, descripcion)
        # TODO 1: agrega el nodo al final sin perder los anteriores
        # Reto individual (versión 11): evita registrar dos veces un mismo código
        if self.cabeza is None:
            self.cabeza = nuevo
            return True
        actual = self.cabeza
        while True:
            if actual.codigo == codigo:
                print(f"Aviso: el código {codigo} ya está registrado. No se agregó.")
                return False
            if actual.siguiente is None:
                break
            actual = actual.siguiente
        actual.siguiente = nuevo
        return True

    def mostrar(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.codigo, actual.descripcion)
            actual = actual.siguiente

class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, elemento):
        # TODO 2: agrega el elemento a la cima
        self.items.append(elemento)

    def desapilar(self):
        # TODO 3: devuelve y elimina el último elemento;
        # controla el caso de pila vacía
        if len(self.items) == 0:
            print("La pila está vacía.")
            return None
        return self.items.pop()

class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, elemento):
        # TODO 4: agrega el elemento al final
        self.items.append(elemento)

    def desencolar(self):
        # TODO 5: devuelve y elimina el primer elemento;
        # controla el caso de cola vacía
        if len(self.items) == 0:
            print("La cola está vacía.")
            return None
        return self.items.pop(0)

# Agrega tus pruebas debajo. Usa los datos asignados en tu versión.

# Versión 11 - Gestión de solicitudes - Tienda de ropa
# Datos de prueba sugeridos: R01 Camisa, R02 Pantalón, R03 Chaqueta

lista = ListaEnlazada()
pila = Pila()
cola = Cola()

opcion = ""
while opcion != "6":
    print("\n===== TIENDA DE ROPA - GESTIÓN DE SOLICITUDES =====")
    print("1. Registrar solicitud")
    print("2. Mostrar lista enlazada")
    print("3. Desencolar solicitud (cola - FIFO)")
    print("4. Desapilar solicitud (pila - LIFO)")
    print("5. Ver pendientes en cola y pila")
    print("6. Salir")
    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        codigo = input("Código (ej. R01): ").strip().upper()
        descripcion = input("Descripción (ej. Camisa): ").strip()
        if codigo == "" or descripcion == "":
            print("Debes escribir código y descripción.")
        elif lista.agregar(codigo, descripcion):
            # Solo se encola y apila si no estaba repetido (reto individual)
            cola.encolar(codigo + " " + descripcion)
            pila.apilar(codigo + " " + descripcion)
            print("Solicitud", codigo, "registrada, encolada y apilada.")

    elif opcion == "2":
        print("--- Lista enlazada ---")
        if lista.cabeza is None:
            print("La lista está vacía.")
        else:
            lista.mostrar()

    elif opcion == "3":
        elemento = cola.desencolar()
        if elemento is not None:
            print("Desencolado (primero que entró):", elemento)

    elif opcion == "4":
        elemento = pila.desapilar()
        if elemento is not None:
            print("Desapilado (último que entró):", elemento)

    elif opcion == "5":
        print("Pendientes en cola:", cola.items)
        print("Pendientes en pila:", pila.items)

    elif opcion == "6":
        print("Programa finalizado.")

    else:
        print("Opción no válida.")
