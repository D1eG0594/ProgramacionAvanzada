import math


class FormaGeometrica:
    def area(self):
        pass

    def perimetro(self):
        pass

class Cuadrado(FormaGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado
    
    def perimetro(self):
        return 4 * self.lado
    
class Circulo(FormaGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return (math.pi) * (self.radio**2)
    
    def perimetro(self):
        return 2 * math.pi * self.radio
    
class Triangulo(FormaGeometrica):
    def __init__(self, base, altura, lado1, lado2, lado3):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def area(self):
        return 0.5*self.base*self.altura
    
    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3