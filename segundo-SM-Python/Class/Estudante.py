class Estudante: #NOME DA CLASSE
    def __init__(self,nome,idade,nota): 
        self.nome = nome
        self.idade = idade
        self.nota = nota

    def get_grade(self):
        print(self.nota)

e1 = Estudante("luis" ,  20,30)
print(e1.nome)
