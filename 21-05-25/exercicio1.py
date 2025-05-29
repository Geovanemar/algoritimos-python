print("=======BEM VINDO, CADASTRO DO CLIENTE=======")
while True:
    cadastro = []

    
    while True:
    
        nome = input("Digite seu nome: ")
        if nome.isdigit():
            print(" INVALIDO!!! ")
        else:
            cadastro.append(nome)    
        break
    while True:
        
        sobrenome =  input("Digite seu sobrenome: " )
        if sobrenome.isdigit():
                print("Invalido")
        else:
         cadastro.append(sobrenome)
        break

    while True:    
        RG = (input("informe seu RG:"))
        if not RG.isdigit() and len(RG) < 6:
                print(" O NUMERO DO CPF É INVALIDO ")
        else:
                cadastro.append(RG)
                break     
        
    while True:    
          CPF = (input("informe seu CPF: "))
          if not CPF.isdigit() and len(CPF) < 11:
                print(" O NUMERO DO CPF É INVALIDO ")
          else:
                cadastro.append(CPF)
                break    

    while True:
       end = input("Digite seu endereço: ")
       if end.isdigit():
            print("Endereço invalido ")
       else:
            cadastro.append(end)
            break     
       
    while True:   
       Tel = (input("informe seu telefone: "))
       if not Tel.isdigit() and len(Tel) < 10:
             print(" NUMERO DE TELEFONE INVALIDO ")
       else:
            cadastro.append(Tel)
            break 

    while True:
        idade = int(input("Digite sua idade: "))
        if   idade < 0 and idade > 120:
             print("Idade Invalida para embarcar")
        else:
            cadastro.append(idade)
            break     

    break

print("======CADASTRO DA PASSAGEM======")

while True:
    cadastro_passagem = []

    while True:
        destino = input("Informe seu destino: ")
        if destino.isdigit():
             print("INVALIDO")
        else:
             cadastro_passagem(destino)
             break

    while True:         
        destino_do_voo = input("Informe seu destino: ")
        if destino_do_voo.isdigit():
             print("INVALIDO")
        else:
             cadastro_passagem(destino_do_voo)
             break
    input("Duração do voo:")
    input("valor da passagem:")
    input("desconto de (5%):")


    

