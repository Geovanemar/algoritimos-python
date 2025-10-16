class Pessoa:
    def __init__(self, nome):
        self.nome = nome


class Conta(Pessoa):
    def __init__(self, nome, num_conta, senha, agencia):
        super().__init__(nome)
        self.num_conta = num_conta
        self.senha = senha
        self.agencia = agencia
        self.saldo = 0
        self.extrato = []

    def autenticar(self, agencia, num_conta, senha):
        return self.agencia == agencia and self.num_conta == num_conta and self.senha == senha

    def depositar(self, agencia, num_conta, valor):
        if self.num_conta == num_conta and self.agencia == agencia:
            if valor > 0:
                self.saldo += valor
                self.extrato.append(f"Depósito:  {valor:.2f}")
                print("Depósito realizado ")
            else:
                print("Valor inválido .")
        else:
            print("Agência ou conta inválida.")

    def sacar(self, agencia, num_conta, valor, senha):
        if self.autenticar(agencia, num_conta, senha):
            if valor > 0 and valor <= self.saldo:
                self.saldo -= valor
                self.extrato.append(f"Saque:  {valor:.2f}")
                print("Saque realizado com sucesso!")
            else:
                print("Saldo insuficiente ou valor inválido.")
        else:
            print("Autenticação falhou.")

    def consultar_saldo(self, agencia, num_conta, senha):
        if self.autenticar(agencia, num_conta, senha):
            print(f"Saldo atual: R$ {self.saldo:.2f}")
        else:
            print("Autenticação falhou.")

    def consultar_extrato(self, agencia, num_conta, senha):
        if self.autenticar(agencia, num_conta, senha):
            print("\n==== Extrato da Conta ====")
            if len(self.extrato) == 0:
                print("Nenhuma movimentação registrada.")
            else:
                for movimento in self.extrato:
                    print(movimento)
            print(f"Saldo final: R$ {self.saldo:.2f}")
            print("==========================")
        else:
            print("Autenticação falhou.")


contas = []

def encontrar_contas(agencia, num_conta):
    for conta in contas:
        if conta.agencia == agencia and conta.num_conta == num_conta:
            return conta
    return None


def menu():
    while True:
        print("\n====== Banco Já Pode Aplicar ======")
        print("1. Cadastrar conta")
        print("2. Consultar Saldo")
        print("3. Consultar Extrato")
        print("4. Sacar Dinheiro")
        print("5. Depositar Dinheiro")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do titular: ")
            agencia = input("Número da agência: ")
            num_conta = input("Número da conta: ")
            senha = input("Defina uma senha: ")

            if encontrar_contas(agencia, num_conta):
                print("Já existe uma conta com essa agência e número.")
            else:
                conta = Conta(nome, num_conta, senha, agencia)
                contas.append(conta)
                print("Conta cadastrada com sucesso!")

        elif opcao == "2":
            agencia = input("Agência: ")
            num_conta = input("Conta: ")
            senha = input("Senha: ")
            conta = encontrar_contas(agencia, num_conta)
            if conta:
                conta.consultar_saldo(agencia, num_conta, senha)
            else:
                print("Conta não encontrada.")

        elif opcao == "3":
            agencia = input("Agência: ")
            num_conta = input("Conta: ")
            senha = input("Senha: ")
            conta = encontrar_contas(agencia, num_conta)
            if conta:
                conta.consultar_extrato(agencia, num_conta, senha)
            else:
                print("Conta não encontrada.")

        elif opcao == "4":
            agencia = input("Agência: ")
            num_conta = input("Conta: ")
            senha = input("Senha: ")
            try:
                valor = float(input("Valor do saque: "))
                conta = encontrar_contas(agencia, num_conta)
                if conta:
                    conta.sacar(agencia, num_conta, valor, senha)
                else:
                    print("Conta não encontrada.")
            except ValueError:
                print("Valor inválido. Digite um número.")

        elif opcao == "5":
            agencia = input("Agência: ")
            num_conta = input("Conta: ")
            try:
                valor = float(input("Valor do depósito: "))
                conta = encontrar_contas(agencia, num_conta)
                if conta:
                    conta.depositar(agencia, num_conta, valor)
                else:
                    print("Conta não encontrada.")
            except ValueError:
                print("Valor inválido. Digite um número.")

        elif opcao == "6":
            print("Saindo do sistema. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()



        
     
