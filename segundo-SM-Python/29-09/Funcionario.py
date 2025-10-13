class Funcionario:
    def __init__(self,nome,login,senha):
        self.nome = nome
        self.login = login
        self.senha = senha

    def logar(self):
        print(f"{self.nome} logado com sucesso") 

    def alterar_senha(self,nova_senha):
        self.senha = nova_senha
        return True


f1 = Funcionario("Geovane, Martins, 090769")
f2 = Funcionario("Geovane, Correia, 22022007")

