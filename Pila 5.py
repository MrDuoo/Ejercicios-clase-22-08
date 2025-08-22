pilaFia = []

# Ingresar nombres
for i in range(3):
    nom = input(f"Ingrese el nombre {i+1}: ")
    pilaFia.append(nom)

print("\nPila inicial:", pilaFia)

eliminar = []

# LIFO: elimina el último ingresado
if pilaFia:
    eliminar.append(("LIFO", pilaFia.pop()))

# FIFO: elimina el primero ingresado (de la misma lista)
if pilaFia:
    eliminar.append(("FIFO", pilaFia.pop(0)))

print("\nEliminados:")
for modo, nom in eliminar:
    print(f" - {modo}: {nom}")

print("\nPila final:", pilaFia)