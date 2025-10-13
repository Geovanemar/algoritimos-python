class Passagem:
    def __init__(self, preco, assento):
        self.preco = preco
        self.assento = assento

    def alterar_preco(self, novo_preco):
        self.preco = novo_preco
        print(f"Preço alterado para R${self.preco:.2f}")

    def escolher_assento(self, novo_assento):
        self.assento = novo_assento
        print(f"Assento escolhido: {self.assento}")


class PassagemAviao(Passagem):
    def __init__(self, preco, assento, portao_embarque, checkin):
        super().__init__(preco, assento)
        self.portao_embarque = portao_embarque
        self.checkin = checkin

    def decolar(self):
        if self.checkin:
            print(f"O avião está decolando! Portão de embarque: {self.portao_embarque} 🛫")
        else:
            print("Você precisa fazer o check-in antes de decolar!")


class PassagemBus(Passagem):
    def __init__(self, preco, assento, placa, leito):
        super().__init__(preco, assento)
        self.placa = placa
        self.leito = leito

    def abastecer(self):
        print(f"O ônibus de placa {self.placa} está sendo abastecido. 🚌")


passagem1 = Passagem(150, "12A")
passagem1.escolher_assento("14B")
passagem1.alterar_preco(180)

aviao = PassagemAviao(800, "7C", "Portão 5", True)
aviao.decolar()

bus = PassagemBus(120, "22", "ABC-1234", True)
bus.abastecer()
