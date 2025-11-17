from Cliente import Cliente

while True:
    print("SysPerkal")
    print("*"*30)
    print("Selecione uma opção: ")
    opçao = input("\t 1 - Cadastrar um cliente\n\t 2 - Listar Clientes\n\t 3 - sair ")

    if opçao == "0":
        break

    if opçao == "1":
        cli = Cliente()
        cli.nome = input("Digite o nome do cliente: ")
        cli.cpf = input("Digite o cpf: ")
        cli.fone = input("Digite o fone: ")
        cli.cidade = input("Digite a Cidade: ")
        result = cli.cadastrar()
        if result == True:
            print("Cadastrado com Sucesso ")

    if opçao == "2":
        cli = Cliente()
        result = cli.buscar()
        for cliente in result:
            print(f"ID: {Cliente[0]} Nome: {Cliente[1]}  CPF: {Cliente[2]}  Fone: {Cliente[3]}  Cidade: {Cliente[4]}" )
                     
