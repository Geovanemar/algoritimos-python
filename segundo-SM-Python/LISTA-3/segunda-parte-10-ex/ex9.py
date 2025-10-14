class Compra:
    def __init__(self, numero, produto, valor):
        self.numero = numero
        self.produto = produto
        self.valor = valor
        self.valor_total = 0

    def calcular_valor_total(self):
        icms = self.valor * 0.17
        frete = self.valor * 0.05
        self.valor_total = self.valor + icms + frete
        print(f"Valor total (com ICMS e frete): R${self.valor_total:.2f}")
        return self.valor_total


class CompraAvista(Compra):
    def __init__(self, numero, produto, valor, desconto):
        super().__init__(numero, produto, valor)
        self.desconto = desconto

    def calcular_valor_total(self):
        icms = self.valor * 0.17
        frete = self.valor * 0.05
        total = self.valor + icms + frete
        desconto_valor = total * (self.desconto / 100)
        self.valor_total = total - desconto_valor
        print(f"Valor total à vista (com desconto de {self.desconto}%): R${self.valor_total:.2f}")
        return self.valor_total

    def get_desconto(self):
        return self.desconto

    def set_desconto(self, novo_desconto):
        self.desconto = novo_desconto
        print(f"Desconto atualizado para {self.desconto}%")


class CompraParcelada(Compra):
    def __init__(self, numero, produto, valor, parcelas):
        super().__init__(numero, produto, valor)
        self.parcelas = parcelas

    def simular_numero_de_parcelas(self):
        total = self.calcular_valor_total()
        valor_parcela = total / self.parcelas
        print(f"Compra parcelada em {self.parcelas}x de R${valor_parcela:.2f}")
        return valor_parcela

    def get_parcelas(self):
        return self.parcelas

    def set_parcelas(self, novas_parcelas):
        self.parcelas = novas_parcelas
        print(f"Número de parcelas atualizado para {self.parcelas}")


compra1 = Compra(101, "Notebook", 3500)
compra1.calcular_valor_total()

avista = CompraAvista(102, "Smartphone", 2500, 10)
avista.calcular_valor_total()

parcelada = CompraParcelada(103, "TV 55''", 4000, 5)
parcelada.simular_numero_de_parcelas()
