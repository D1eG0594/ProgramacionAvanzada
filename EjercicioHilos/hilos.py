import threading
import random
import time

class Triciclo(threading.Thread):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
        self.posicion = 0
        self.avances = 0

    def avanzar(self):
        avance = random.randint(1, 5)  # Avance aleatorio entre 1 y 5 espacios
        self.posicion += avance
        self.avances += 1
        print(f"{self.nombre} ha avanzado a la posición {self.posicion}")

    def run(self):
        meta = 100
        while self.posicion < meta:
            self.avanzar()
            time.sleep(0.1)  # Pequeño retraso para visualizar la carrera
        print(f"{self.nombre} ha llegado a la meta en la posición {self.posicion} después de {self.avances} avances!")

def main():
    participantes = []
    for i in range(10):
        triciclo = Triciclo(f"Triciclo {i+1}")
        participantes.append(triciclo)
    
    # Iniciar la carrera
    print("¡Comienza la carrera!")
    for participante in participantes:
        participante.start()

    # Esperar a que todos los participantes lleguen a la meta
    for participante in participantes:
        participante.join()

    print("La carrera ha terminado!")
    
    # Ordenar los triciclos que llegaron a la meta por cantidad de avances (menor a mayor)
    triciclos_ordenados = sorted(participantes, key=lambda x: x.avances)

    # Imprimir la posición relativa de cada triciclo basándonos en el orden de llegada
    print("\nPosiciones finales:")
    for i, triciclo in enumerate(triciclos_ordenados):
        posicion_relativa = "primero" if i == 0 else "segundo" if i == 1 else "tercero" if i == 2 else f"{i+1}º"
        print(f"{triciclo.nombre} llegó {posicion_relativa}.")

if __name__ == "__main__":
    main()