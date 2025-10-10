class Pessoa:
    def __init__(self, matricula, nome, idade):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade


class Aluno(Pessoa):
    def __init__(self, matricula, nome, idade, notas=None):
        super().__init__(matricula, nome, idade)
        self.notas = notas if notas is not None else []
        self.media = 0.0

    def calcular_media(self):
        if len(self.notas) > 0:
            self.media = sum(self.notas) / len(self.notas)
        else:
            self.media = 0.0
        print(f"A média do aluno {self.nome} é {self.media:.2f}")

    def estudar(self):
        print(f"O aluno {self.nome} está estudando para melhorar suas notas.")


class Professor(Pessoa):
    def __init__(self, matricula, nome, idade, formacao, disciplina, carga_horaria, salario):
        super().__init__(matricula, nome, idade)
        self.formacao = formacao
        self.disciplina = disciplina
        self.carga_horaria = carga_horaria
        self.salario = salario

    def lecionar(self):
        print(f"O professor {self.nome} está lecionando a disciplina de {self.disciplina}.")

    def mostrar_dados(self):
        print(f"Professor: {self.nome}\nFormação: {self.formacao}\nDisciplina: {self.disciplina}\n"
              f"Carga Horária: {self.carga_horaria}h\nSalário: R${self.salario:.2f}\n")



if __name__ == "__main__":
    aluno1 = Aluno(101, "Maria Silva", 20, [8.5, 7.0, 9.0])
    professor1 = Professor(201, "João Souza", 40, "Engenharia", "Matemática", 20, 3500.00)

    aluno1.estudar()
    aluno1.calcular_media()
    print()

    professor1.lecionar()
    professor1.mostrar_dados()
