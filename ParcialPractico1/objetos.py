import random



class Persona:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

class Salud:
    def __init__(self, fecha_nacimiento, peso, altura, objetivo, condiciones_medicas):
        self.fecha_nacimiento = fecha_nacimiento
        self.peso = peso
        self.altura = altura
        self.objetivo = objetivo
        self.condiciones_medicas = condiciones_medicas

class Rutina:
    def __init__(self, tipo, duracion, intensidad):
        self.tipo = tipo
        self.duracion = duracion
        self.intensidad = intensidad

    def __str__(self):
        return f"Tipo: {self.tipo}, Duración: {self.duracion}, Intensidad: {self.intensidad}"

class Cliente(Persona, Salud):
    def __init__(self, nombre, telefono, email, fecha_nacimiento, peso, altura, objetivo, condiciones_medicas):
        Persona.__init__(self, nombre, telefono, email)
        Salud.__init__(self, fecha_nacimiento, peso, altura, objetivo, condiciones_medicas)
        self.rutina = None

    def asignar_rutina(self, rutina):
        tipos_rutina = ["Cardio", "Fuerza", "Flexibilidad"]
        duraciones = ["30 minutos", "45 minutos", "1 hora"]
        intensidades = ["Baja", "Moderada", "Alta"]
        
        # Seleccionar rutina aleatoria basada en el objetivo
        if self.objetivo == "Perder peso":
            rutina = Rutina("Cardio", random.choice(duraciones), "Moderada")
            self.rutina = rutina
        elif self.objetivo == "Ganar músculo":
            rutina = Rutina("Fuerza", random.choice(duraciones), "Alta")
            self.rutina = rutina
        else:
            rutina = Rutina("Flexibilidad", random.choice(duraciones), "Moderada")
            self.rutina = rutina
    def ver_rutina(self):
        if self.rutina:
            return str(self.rutina)
        else:
            return "Aún no se ha asignado una rutina."

        