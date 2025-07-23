while True:
    clientes = []

    while True:
        nome = (input("informe seu nome: "))
        if nome.isdigit():
              print(" INVALIDO!!! ")
        else:
            clientes.append(nome)
            break      

    while True:
            CPF = (input("informe seu CPF: "))
            if not CPF.isdigit() and len(CPF) < 11:
                print(" O NUMERO DO CPF É INVALIDO ")
            else:
                clientes.append(CPF)
                break    
    while True:
        RG = (input("informe seu RG:"))
        if not RG.isdigit() and len(RG) < 6:
                print(" O NUMERO DO CPF É INVALIDO ")
        else:
                clientes.append(RG)
                break     
    while True:
        Tel = (input("informe seu telefone: "))
        if not Tel.isdigit() and len(Tel) < 10:
             print(" NUMERO DE TELEFONE INVALIDO ")
        else:
             clientes.append(Tel)
             break     
    while True:
             
        num_agencia = (input("informe o numero da agencia: "))
        if not num_agencia.isdigit() and len(num_agencia) != 3:
             print(" NUMERO DA AGENCIA INVALIDO ")
        else:
             clientes.append(num_agencia)
             break
    while True:
                  
        num_conta = (input("informe o numero da conta: "))
        if not num_conta.isdigit() and len(num_conta) != 6:
             print(" O NUMERO DA CONTA É INVALIDO ")
        else:
             clientes.append(num_conta)
             break
    while True:         
        sal_inicial = float(input("informe o seu saldo inicial: "))
        if sal_inicial < 0:
             print("NÃO É POSSIVEL REALIZAR O CADASTRO ")
        else:
             clientes.append(sal_inicial)
             break     
        
    while True:
        print(" CADASTRO REALIZADO!!! ")

        lista_bamco = input("1 = Ver Saldo , 2 = Deposito , 3 = Sacar , 4 Sair: " )

        print("CADASTRO REALIZADO!!", "\nNOME: ", clientes[0], "\nCPF: " , clientes[1], "\nRG: ", clientes[2] , "\nTEL: " , clientes[3], "\nNumero da agencia: ", clientes[4], "\nNumero da conta: ", clientes[5], "\nSalario Inicial: ", clientes[6] )

        if lista_bamco == "1":
             print("Saldo", clientes[6])

        if lista_bamco == "2":
          Deposito = float(input("valor do deposito: "))
          clientes[6] = clientes[6] + Deposito

        if lista_bamco == "3":
          sacar = float(input("Valor do saque: "))
          if sacar > clientes[6]:
               print("valor acima do que existe")
          else:
               clientes[6] = clientes[6] - sacar     

        if lista_bamco == "4":
             print("Sair", clientes[6] )  

             break        


   

