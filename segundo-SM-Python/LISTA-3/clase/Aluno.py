class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def exibirMatricula(self):
        return self.matricula 
    def exibirNome(self):
        return self.nome


aluno1 = Aluno("Geovane", 56568)


print(aluno1.exibirMatricula())
print(aluno1.exibirNome())
