from abc import ABC, abstractmethod
from math import pi

class Poligono(ABC):
    def __init__(self, qtd_lado):
        self.qtd_lado = qtd_lado
    
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Quadrado(Poligono):

    def __init__(self, lado):
        super().__init__(4)
        self.lado = lado

    def area(self):
        return self.lado ** 2
    
    def perimetro(self):
        return self.lado * self.qtd_lado

class Circulo(Poligono):

    def __init__(self, raio):
        super().__init__(1)
        self.raio = raio

    def area(self):
        return pi * (self.raio ** 2)
    
    def perimetro(self):
        return 2 * pi * self.raio