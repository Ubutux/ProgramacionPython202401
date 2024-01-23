semaforo = input("Ingrese el estado del semáforo (verde/rojo/amarillo): ")

# Convertimos el estado del semáforo a minúsculas
semaforo = semaforo.lower()

# Si el semáforo está en verde, cruzamos la calle
if semaforo == "verde":
    print("Puede cruzar la calle")

# Si el semáforo está en rojo o amarillo, no cruzamos la calle
else:
    print("No puede cruzar la calle")

