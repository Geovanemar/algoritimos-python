class Funcionario:
    def __init__(self, nome, sobrenome, horas_trabalhadas, valor_hora):

        self.nome = nome
        self.sobrenome = sobrenome
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def nomeCompleto(self):
            print("nome completo {self.nome} , {self.sobrenome}" )    

    def calcularSalario(self):
        salario = self.horas_trabalhadas * self.valor_hora
        print(f"Salario do mes: {salario: .2f}")


    def incrementarHoras(self, horas_adicionais):
        self.horas_trabalhadas += horas_adicionais
        print(f"horas trabalhadas atualizadas: {self.horas_trabalhadas}")    

fun1 = Funcionario("geovane", "martins", 200, 40)      
print(fun1.nomeCompleto())          
print(fun1.calcularSalario())    
print(fun1.incrementarHoras(10))    
print(fun1.calcularSalario())  