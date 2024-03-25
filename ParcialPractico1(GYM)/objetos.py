import random

# Definición de la clase Persona para representar a una persona
class Persona:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

# Definición de la clase Salud para representar la salud de una persona
class Salud:
    def __init__(self, fecha_nacimiento, peso, altura, objetivo, condiciones_medicas):
        self.fecha_nacimiento = fecha_nacimiento
        self.peso = peso
        self.altura = altura
        self.objetivo = objetivo
        self.condiciones_medicas = condiciones_medicas

# Definición de la clase Rutina para representar una rutina de ejercicios
class Rutina:
    def __init__(self, tipo, duracion, intensidad):
        self.tipo = tipo
        self.duracion = duracion
        self.intensidad = intensidad

# Definición de la clase Cliente para representar a un cliente, que es una persona con datos de salud
class Cliente(Persona, Salud):
    def __init__(self, nombre, telefono, email, fecha_nacimiento, peso, altura, objetivo, condiciones_medicas):
        Persona.__init__(self, nombre, telefono, email)
        Salud.__init__(self, fecha_nacimiento, peso, altura, objetivo, condiciones_medicas)

    # Método para asignar una rutina de ejercicios basada en el objetivo de salud del cliente
    def asignar_rutina(self):
        # Definición de los ejercicios disponibles y sus duraciones asociadas
        tipos_rutina = {
            "Perder peso": ["Correr", "Saltar la cuerda", "Burpees", "Sentadillas"],
            "Ganar músculo": ["Press de banca", "Peso muerto", "Sentadillas con barra", "Dominadas"],
            "Flexibilidad": ["Estiramientos de piernas", "Estiramientos de espalda", "Estiramientos de brazos", "Yoga"]
        }
        
        duraciones = {
            "Correr": ["30 minutos", "45 minutos", "1 hora"],
            "Saltar la cuerda": ["10 minutos", "15 minutos", "20 minutos"],
            "Burpees": ["5 minutos", "10 minutos", "15 minutos"],
            "Sentadillas": ["20 repeticiones", "30 repeticiones", "40 repeticiones"],
            "Press de banca": ["3 series de 10 repeticiones", "4 series de 8 repeticiones", "5 series de 5 repeticiones"],
            "Peso muerto": ["3 series de 8 repeticiones", "4 series de 6 repeticiones", "5 series de 5 repeticiones"],
            "Sentadillas con barra": ["3 series de 12 repeticiones", "4 series de 10 repeticiones", "5 series de 8 repeticiones"],
            "Dominadas": ["3 series de 5 repeticiones", "4 series de 4 repeticiones", "5 series de 3 repeticiones"],
            "Estiramientos de piernas": ["10 minutos", "15 minutos", "20 minutos"],
            "Estiramientos de espalda": ["10 minutos", "15 minutos", "20 minutos"],
            "Estiramientos de brazos": ["10 minutos", "15 minutos", "20 minutos"],
            "Yoga": ["30 minutos", "45 minutos", "1 hora"]
        }

        ejercicios = tipos_rutina.get(self.objetivo, [])  # Obtener la lista de ejercicios según el objetivo
        if not ejercicios:
            return None  # Devolver None si el objetivo no está definido

         # Se genera la rutina seleccionando aleatoriamente ejercicios y duraciones
        rutina = []
        for ejercicio in ejercicios:
            duracion = random.choice(duraciones[ejercicio])
            rutina.append((ejercicio, duracion))

        return rutina

        