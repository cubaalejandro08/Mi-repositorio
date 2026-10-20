Evaluación práctica — Versión 11

Reto: gestión de solicitudes de una tienda de ropa usando una lista enlazada, una pila y una cola. Todo funciona en memoria, sin bases de datos ni SQL.

Datos de prueba
R01: Camisa
R02: Pantalón
R03: Chaqueta
Qué hace el programa
Lista enlazada: agrega cada nodo al final sin perder los anteriores.
Pila (LIFO): apilar y desapilar; si la pila está vacía, avisa y devuelve None.
Cola (FIFO): encolar y desencolar; si la cola está vacía, avisa y devuelve None.
Reto individual: no deja registrar dos veces el mismo código en la lista.
Cómo ejecutar
python main.py

El programa muestra un menú y pide por teclado el código y la descripción de cada solicitud. Cada solicitud registrada se agrega a la lista enlazada, se encola y se apila. Si el código ya existe, no se registra.
