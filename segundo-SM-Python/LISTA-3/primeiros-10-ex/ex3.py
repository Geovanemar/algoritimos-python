class Aluno:
    def __init__(self, nome, ra, nota1, nota2, nota3, nota4):
        self.nome = nome
        self.ra = ra
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4

    def mostrar_situação(self):
        media = (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4


        print(f"aluno {self.nome}")
        print(f"media do aluno  {media:.2f}")

        if media >= 7:
            print("Aprovado")
        
        elif  5 <= media < 7:
            print(" Exame")
        
        else:
            print("Reprovado")

aluno1 = Aluno("Geovane Martins", 453654 , 7.0, 2.0, 10.0, 6.5)
aluno1.mostrar_situação()
         
