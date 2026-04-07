class Imovel:
    def __init__(self, inscricao_municipal, valor_aluguel, iptu):
        self.inscricao_municipal = inscricao_municipal
        self.valor_aluguel = valor_aluguel
        self.iptu = iptu

    def obter_parcela_IPTU(self, parcelas):
        valor_parcela = self.iptu / parcelas
        print(f"O IPTU será pago em {parcelas} parcelas de R${valor_parcela:.2f}")
        return valor_parcela

    def set_valor_aluguel(self, novo_valor):
        self.valor_aluguel = novo_valor
        print(f"O novo valor do aluguel é R${self.valor_aluguel:.2f}")


class Casa(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu, quartos, piscina, churrasqueira):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.quartos = quartos
        self.piscina = piscina
        self.churrasqueira = churrasqueira

    def mostrar_detalhes(self):
        print(f"Casa com {self.quartos} quartos. Piscina: {self.piscina}, Churrasqueira: {self.churrasqueira}")


class Apartamento(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu, quartos, elevador, area_lazer):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.quartos = quartos
        self.elevador = elevador
        self.area_lazer = area_lazer

    def mostrar_detalhes(self):
        print(f"Apartamento com {self.quartos} quartos. Elevador: {self.elevador}, Área de lazer: {self.area_lazer}")


class Terreno(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu, area_m2, murado):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.area_m2 = area_m2
        self.murado = murado

    def mostrar_detalhes(self):
        print(f"Terreno de {self.area_m2} m². Murado: {self.murado}")


class Chacara(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu, quartos, piscina, area_verde):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.quartos = quartos
        self.piscina = piscina
        self.area_verde = area_verde

    def mostrar_detalhes(self):
        print(f"Chácara com {self.quartos} quartos. Piscina: {self.piscina}, Área verde: {self.area_verde} m²")


casa = Casa("12345", 2500, 1200, 3, True, True)
apartamento = Apartamento("54321", 2000, 1000, 2, True, True)
terreno = Terreno("98765", 800, 600, 350, False)
chacara = Chacara("67890", 3500, 2000, 4, True, 800)

imoveis = [casa, apartamento, terreno, chacara]

for i in imoveis:
    i.mostrar_detalhes()
    i.obter_parcela_IPTU(4)
    print("-" * 50)
