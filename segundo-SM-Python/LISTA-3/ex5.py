import math
 
class Circulo:
    def __init__(self, raio):

        self.raio = raio

    def imprimirRaio(self):
        print(f"raio do circulo: {self.raio}")


    def CalcularArea(self):
        area = math.pi * (self.raio ** 2)
        print(f"Area do circulo: {area: .2f}")

    
    def calcularCircunferencia(self):
        circunferencia = 2 * math.pi * self.raio
        print(f"Circunferência do círculo: {circunferencia:.2f}")


c1 = Circulo(5) 
print(c1.imprimirRaio())   
print(c1.CalcularArea())
print(c1.calcularCircunferencia())    



