class Titular:
    def __init__(self, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco

    def mostrar_dados(self):
        print(f"Titular: {self.nome} | CPF: {self.cpf} | Endereço: {self.endereco}")


class Conta:
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso. Novo saldo: R${self.saldo:.2f}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente para saque.")

    def mostrar_saldo(self):
        print(f"Conta {self.numero} | Saldo atual: R${self.saldo:.2f}")


class ContaCorrente(Conta):
    def __init__(self, numero, titular, saldo=0, limite=500):
        super().__init__(numero, titular, saldo)
        self.limite = limite

    def usar_limite(self, valor):
        total_disponivel = self.saldo + self.limite
        if valor <= total_disponivel:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com limite. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Limite insuficiente para esta operação.")


class ContaPoupanca(Conta):
    def __init__(self, numero, titular, saldo=0, rendimento=0.005):
        super().__init__(numero, titular, saldo)
        self.rendimento = rendimento

    def aplicar_rendimento(self):
        ganho = self.saldo * self.rendimento
        self.saldo += ganho
        print(f"Rendimento de R${ganho:.2f} aplicado. Novo saldo: R${self.saldo:.2f}")


class FundoDeInvestimento(Conta):
    def __init__(self, numero, titular, saldo=0, taxa_adm=0.02):
        super().__init__(numero, titular, saldo)
        self.taxa_adm = taxa_adm

    def aplicar_rendimento(self, rentabilidade):
        ganho = (self.saldo * rentabilidade) - (self.saldo * self.taxa_adm)
        self.saldo += ganho
        print(f"Fundo atualizado com rentabilidade líquida. Saldo: R${self.saldo:.2f}")


titular1 = Titular("Ana Souza", "123.456.789-00", "Rua das Flores, 123")
titular2 = Titular("João Lima", "987.654.321-00", "Av. Brasil, 987")

corrente = ContaCorrente(1001, titular1, 1500)
poupanca = ContaPoupanca(2002, titular2, 3000)
fundo = FundoDeInvestimento(3003, titular1, 5000)

titular1.mostrar_dados()
corrente.mostrar_saldo()
corrente.sacar(1800)
corrente.usar_limite(200)
corrente.depositar(1000)

poupanca.aplicar_rendimento()
fundo.aplicar_rendimento(0.05)
