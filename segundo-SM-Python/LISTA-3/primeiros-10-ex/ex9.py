class Carro:
    def __init__(self, marca, modelo, cor, ano, valor, consumo, nivel=0):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.valor = valor
        self.consumo = consumo  
        self.nivel = nivel      

    def abastecer(self, litros):
        self.nivel += litros
        print(f"Tanque abastecido com {litros} L. Nível atual: {self.nivel:.2f} L")

    def andar(self, distancia):
        litros_necessarios = distancia / self.consumo
        if litros_necessarios > self.nivel:
            print("Combustível insuficiente para percorrer essa distância!")
        else:
            self.nivel -= litros_necessarios
            print(f"O carro percorreu {distancia} km e consumiu {litros_necessarios:.2f} L.")
            print(f"Nível atual de combustível: {self.nivel:.2f} L")

    def verificar_nivel(self):
        print(f"Nível atual do tanque: {self.nivel:.2f} L")

    def calcular_imposto(self):
        imposto = self.valor * 0.035
        print(f"IPVA (3,5% do valor do carro): R$ {imposto:.2f}")
        return imposto


carro1 = Carro("Toyota", "Corolla", "Prata", 2020, 95000, 12)

carro1.abastecer(20)
carro1.andar(100)
carro1.verificar_nivel()
carro1.calcular_imposto()
