class Livro:
    def __init__(self, nome, autor, editora, paginas):
        
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas

    def alterar_editora(self, nova_editora):
        print("editora alterada para , {self.editora}")   

    def listar_qntd_pg(self):
        print("quantidade de paginas {self.paginas}")   


Livro1 = Livro("O diario de um banana" , "Geovane Martins" , "editora seila", 256)
print(Livro1.nome, Livro1.autor, Livro1.editora, Livro1.paginas)

        