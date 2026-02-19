class Aluno:

    def __init__(self, nome, ra):
        self.nome = nome
        self.ra = ra

class Universidade:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def adicionar_aluno(self, aluno:object):
        self.alunos.append(aluno)

a1 = Aluno("Geovane", "3213")            
a2 = Aluno("joão", "4322")            
a3 = Aluno("mateus", "7654")            
a4 = Aluno("duda", "5433")            

faculdade = Universidade("SENAC MS")
print(len(faculdade.alunos))
faculdade.adicionar_aluno(a1)
faculdade.adicionar_aluno(a2)
faculdade.adicionar_aluno(a3)
faculdade.adicionar_aluno(a4)
print(len(faculdade.alunos))

print("Alunos da" , faculdade.nome)
for aluno in faculdade.alunos:
    print(f"Nome: {aluno.nome}, Ra: {aluno.ra}")