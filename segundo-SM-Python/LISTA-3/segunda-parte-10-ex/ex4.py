class Ingresso:
    def __init__(self, preco, setor):
        self.preco = preco
        self.setor = setor

    def alterar_preco(self, novo_preco):
        self.preco = novo_preco
        print(f"Preço alterado para R${self.preco:.2f}")

    def mostrar_setor(self):
        print(f"Setor: {self.setor}")


class IngressoVIP(Ingresso):
    def __init__(self, preco, setor, camarote, open_bar, open_food, estacionamento):
        super().__init__(preco, setor)
        self.camarote = camarote
        self.open_bar = open_bar
        self.open_food = open_food
        self.estacionamento = estacionamento

    def pegar_bebida(self):
        if self.open_bar:
            print("Você pegou uma bebida ")
        else:
            print("Esse ingresso não inclui open bar.")

    def acessar_camarote(self):
        if self.camarote:
            print("Acesso do camarote liberado ")
        else:
            print("Este ingresso não dá acesso ao camarote.")


ingresso1 = Ingresso(100, "Pista")
ingresso1.mostrar_setor()
ingresso1.alterar_preco(120)

vip = IngressoVIP(300, "VIP Lounge", True, True, True, False)
vip.mostrar_setor()
vip.pegar_bebida()
vip.acessar_camarote()
