class Funcionario:
    def __init__(self, nome, matricula, salario):
        self.nome = nome
        self.matricula = matricula
        self.salario = salario
        self.pontos = []

    def bater_ponto(self, ponto):
        self.pontos.append(ponto)
        if ponto == 1:
            print(f"{self.nome} bateu o ponto (entrada registrada).")
        else:
            print(f"{self.nome} bateu o ponto (saída registrada).")


class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario, comissao):
        super().__init__(nome, matricula, salario)
        self.comissao = comissao

    def bater_meta(self, vendas):
        if vendas >= 10000:
            bonus = self.comissao * 0.1
            self.salario += bonus
            print(f"{self.nome} bateu a meta! Bônus de R${bonus:.2f} aplicado. Novo salário: R${self.salario:.2f}")
        else:
            print(f"{self.nome} não atingiu a meta de vendas.")


class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario, senha):
        super().__init__(nome, matricula, salario)
        self.senha = senha

    def acessar_sistema(self, senha_digitada):
        if senha_digitada == self.senha:
            print(f"Acesso concedido ao gerente {self.nome}.")
        else:
            print("Senha incorreta. Acesso negado.")


func1 = Funcionario("João", 123, 2500)
func1.bater_ponto(1)
func1.bater_ponto(0)

vendedor = Vendedor("Maria", 456, 3000, 500)
vendedor.bater_ponto(1)
vendedor.bater_meta(12000)

gerente = Gerente("Carlos", 789, 6000, "admin123")
gerente.bater_ponto(1)
gerente.acessar_sistema("admin123")
