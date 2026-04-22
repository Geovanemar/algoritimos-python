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
while True:
    print("======CADASTRO DA PASSAGEM======")

    cadastro_voo = []

    while True:
     destino = input("Informe seu destino:")
     if destino.isdigit():
          print("INVALIDO!")
     else:
        cadastro_voo.append(destino)    
        break    
    while True:
      destino_origem = input("Informe destino de origem:")
      if destino.isdigit():
          print("INVALIDO!")
      else:
        cadastro_voo.append(destino)    
        break    
    while True:
        duração_voo = int(input("Duração do voo:"))
        if duração_voo < 0 and duração_voo > 200:
            print("INVALIDO")
        else:
            cadastro_voo.append(duração_voo)    
            break
    while True:
        valor_passagem = float(input("valor da passagem:"))
        if valor_passagem < 0 and valor_passagem > 1000000:
            print("valor invalido")
        else:
            cadastro_voo.append(valor_passagem)    
            break
    while True:
        desconto = float(input("desconto de (5%):")) 
        desconto = valor_passagem * 0.05
        valor_com_desconto = desconto - valor_passagem
        if valor_passagem > 2000:
            print("desconto de 5%:", valor_com_desconto)
        else:
            cadastro_voo.append(desconto)    
            break   
    break
while True:
     print("======CADASTRO DO AVIÃO======")

     cadastro_avião = []

     while True:
        modelo = input("Modelo do Avião: ")
        if modelo.isdigit():
          print("INVALIDO!")
        else:
         cadastro_avião.append(modelo)    
         break    
     while True:
          ano_avião = input("Ano do Avião: ")
          if ano_avião < 1990 and ano_avião > 2026:
            print(" ANO INVALIDO!")
          else:
           cadastro_avião.append(ano_avião)    
           break  
     while True:
         horas_de_voo = int(input("Horas de voo:"))
         if horas_de_voo < 0 and horas_de_voo > 100:
             print("INVALIDO")
         else:
          cadastro_avião.append(horas_de_voo)
          break  
     while True:
        cor = input("Cor do Avião: ")
        if cor.isdigit():
          print("INVALIDO!")
        else:
         cadastro_avião.append(cor)    
         break  
     while True:
         qtnd_passageiros = int(input("quantidade de passageiros:"))
         if qtnd_passageiros < 0 and horas_de_voo > 300:
             print("INVALIDO")
         else:
          cadastro_avião.append(qtnd_passageiros)
          break    

     break
while True:
     print("======CADASTRO TRIPULAÇÃO======")
     
     Cadastro_tripulação = []
     while True:
        nome = input("Digite seu nome: ")
        if nome.isdigit():
            print(" INVALIDO!!! ")
        else:
            Cadastro_tripulação.append(nome)    
        break
     while True:
        cargo = input("Digite seu cargo: ")
        if cargo.isdigit():
            print(" INVALIDO!!! ")
        else:
            Cadastro_tripulação.append(cargo)    
        break
     while True:
        idade = int(input("Digite sua idade: "))
        if   idade < 0 and idade > 120:
             print("Idade Invalida para embarcar")
        else:
            Cadastro_tripulação.append(idade)
            break  
     while True:
         data_emissão = int(input("Digite a Data de Emissão: "))
         if data_emissão < 0 and data_emissão > 3000:
             print("INVALIDO")
         else:
             Cadastro_tripulação.append(data_emissão)
             break    
     while True:   
       Tel = (input("informe seu telefone: "))
       if not Tel.isdigit() and len(Tel) < 10:
             print(" NUMERO DE TELEFONE INVALIDO ")
       else:
            Cadastro_tripulação.append(Tel)
            break  

                


      
           


