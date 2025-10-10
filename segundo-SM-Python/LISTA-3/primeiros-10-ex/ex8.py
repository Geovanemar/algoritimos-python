class Aluno_Academia:
    def __init__(self, nome, idade, peso, altura, mensalidade=120):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.mensalidade = mensalidade

    def calcular_IMC(self):
        imc = self.peso / (self.altura ** 2)
        print(f"IMC de {self.nome}: {imc:.2f}")
        return imc

    def obter_valor_mensalidade(self):
        if self.idade < 18:
            desconto = 0.20  
            valor_final = self.mensalidade * (1 - desconto)
            print(f"{self.nome} é menor de idade. Mensalidade com desconto: R$ {valor_final:.2f}")
        else:
            valor_final = self.mensalidade
            print(f"{self.nome} é maior de idade. Mensalidade normal: R$ {valor_final:.2f}")
        return valor_final



aluno1 = Aluno_Academia("Lucas", 17, 65, 1.75)
aluno2 = Aluno_Academia("Mariana", 25, 70, 1.68)

print("\n--- Dados dos Alunos ---")
aluno1.calcular_IMC()
aluno1.obter_valor_mensalidade()

print()
aluno2.calcular_IMC()
aluno2.obter_valor_mensalidade()
