from datetime import datetime

class Agenda:
    def __init__(self, dia, mes, ano, anotacao=""):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.anotacao = anotacao

    def validar_data(self):
        try:
            datetime(self.ano, self.mes, self.dia)
            print("Data válida!")
        except ValueError:
            print("Data inválida!")

    def anotar_tarefa(self, nova_anotacao):
        self.anotacao = nova_anotacao
        print("Tarefa anotada com sucesso!")

    def mostrar_anotacao(self):
        data_formatada = f"{self.dia:02d}/{self.mes:02d}/{self.ano}"
        print(f"Data: {data_formatada}")
        print(f"Anotação: {self.anotacao if self.anotacao else 'Nenhuma anotação registrada.'}")


# Exemplo de uso:
agenda1 = Agenda(8, 10, 2025)
agenda1.validar_data()
agenda1.anotar_tarefa("Entregar o relatório do projeto ArduinoSilêncio Hospitalar.")
agenda1.mostrar_anotacao()
