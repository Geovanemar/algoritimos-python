class Pessoa:
    def __init__(self, nome, idade, endereço):
        self.nome = nome
        self.idade = idade
        self.endereço = endereço

    def mostrar_nome(self):
        print(f"Nome: {self.nome} ")    

    def alterar_idade(self, nova_idade):
        self.idade = nova_idade
        print("idade alterada para {self.idade} ")   

    def imprimir_endereço(self):
        print(f"endereço:  {self.endereço}")   
        

p1 = Pessoa("Geovane Martins", 18 , "Rua vilas boas 8798")  

print(p1.nome, p1.idade, p1.endereço)   
   