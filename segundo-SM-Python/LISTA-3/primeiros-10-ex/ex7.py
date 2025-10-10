import math

class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def calcularPerimetro(self):
        perimetro = self.ladoA + self.ladoB + self.ladoC
        return perimetro

    def getMaiorLado(self):
        maior = max(self.ladoA, self.ladoB, self.ladoC)
        return maior

    def calcularArea(self):
       
        p = self.calcularPerimetro() / 2
        area = math.sqrt(p * (p - self.ladoA) * (p - self.ladoB) * (p - self.ladoC))
        return area



print("Informe as medidas do triângulo:")
a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

triangulo = Triangulo(a, b, c)

print("\n--- Resultados ---")
print(f"Perímetro: {triangulo.calcularPerimetro():.2f}")
print(f"Área: {triangulo.calcularArea():.2f}")
print(f"Maior lado: {triangulo.getMaiorLado():.2f}")
