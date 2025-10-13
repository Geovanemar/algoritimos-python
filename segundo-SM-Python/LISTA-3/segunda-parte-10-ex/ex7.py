class Brinquedo:
    def __init__(self, nome, cor, tamanho, preco):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho
        self.preco = preco

    def brincar(self):
        print(f"Estou brincando com {self.nome}.")


class BuzzLightyear(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, tem_lasers):
        super().__init__(nome, cor, tamanho, preco)
        self.tem_lasers = tem_lasers

    def voar(self):
        print(f"{self.nome} está voando pelo espaço! ")

    def brincar(self):
        print(f"Estou brincando com {self.nome}, o patrulheiro espacial!")


class Woody(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, tem_corda):
        super().__init__(nome, cor, tamanho, preco)
        self.tem_corda = tem_corda

    def lancar_corda(self):
        print(f"{self.nome} lançou sua corda com precisão! ")

    def brincar(self):
        print(f"Estou brincando com {self.nome}, o caubói mais famoso do Velho Oeste!")


class Rex(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, dentes_afiados):
        super().__init__(nome, cor, tamanho, preco)
        self.dentes_afiados = dentes_afiados

    def rugir(self):
        print(f"{self.nome} está rugindo! ")

    def brincar(self):
        print(f"Estou brincando com {self.nome}, o dinossauro desajeitado!")


class Jessie(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, chapéu):
        super().__init__(nome, cor, tamanho, preco)
        self.chapeu = chapéu

    def cantar(self):
        print(f"{self.nome} está cantando uma música de cowgirl! 🎵")

    def brincar(self):
        print(f"Estou brincando com {self.nome}, a cowgirl animada!")


class Slinky(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, material):
        super().__init__(nome, cor, tamanho, preco)
        self.material = material

    def esticar(self):
        print(f"{self.nome} está se esticando! ")

    def brincar(self):
        print(f"Estou brincando com {self.nome}, o cachorro-mola divertido!")


buzz = BuzzLightyear("Buzz Lightyear", "Branco e Verde", "Médio", 150.00, True)
woody = Woody("Woody", "Marrom", "Médio", 120.00, True)
rex = Rex("Rex", "Verde", "Grande", 100.00, True)
jessie = Jessie("Jessie", "Vermelho", "Médio", 110.00, True)
slinky = Slinky("Slinky", "Marrom", "Pequeno", 90.00, "metal")

brinquedos = [buzz, woody, rex, jessie, slinky]

for b in brinquedos:
    b.brincar()
