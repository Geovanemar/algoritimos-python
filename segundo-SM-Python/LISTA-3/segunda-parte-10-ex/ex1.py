class Filme:
    def __init__(self, nome, duracao):
        self.nome = nome
        self.duracao = duracao

    def play(self):
        print(f"Reproduzindo o filme: {self.nome} ({self.duracao} minutos)")


class Acao(Filme):
    def __init__(self, nome, duracao):
        super().__init__(nome, duracao)

    def explodir(self):
        print(f"Muita ação! Uma grande explosão aconteceu no filme {self.nome}!")


class Drama(Filme):
    def __init__(self, nome, duracao):
        super().__init__(nome, duracao)

    def emocionar(self):
        print(f"O filme {self.nome} emocionou o público com uma história comovente.")


class Suspense(Filme):
    def __init__(self, nome, duracao):
        super().__init__(nome, duracao)

    def revelar_segredo(self):
        print(f"O segredo foi revelado no filme {self.nome}! Que reviravolta!")



if __name__ == "__main__":
    filme_acao = Acao("Missão Explosiva", 120)
    filme_drama = Drama("Corações Partidos", 110)
    filme_suspense = Suspense("Mistério na Noite", 100)

    filme_acao.play()
    filme_acao.explodir()

    filme_drama.play()
    filme_drama.emocionar()

    filme_suspense.play()
    filme_suspense.revelar_segredo()
