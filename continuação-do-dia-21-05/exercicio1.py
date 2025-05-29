print("=======BEM VINDO, CADASTRO DO CLIENTE=======")
cadastro = []
cadastro_voo = []
cadastro_avião = []
cadastro_tripulação = []
while True:
    
   
    
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

   

    while True:
     destino = input("Informe seu destino:")
     if destino.isdigit():
          print("INVALIDO!")
     else:
        cadastro_voo.append(destino)    
        break    
    while True:
      destino_origem = input("Informe destino de origem:")
      if destino_origem.isdigit():
          print("INVALIDO!")
      else:
        cadastro_voo.append(destino_origem)    
        break    
    while True:
        duração_voo = float(input("Duração do voo:"))
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
        desconto = valor_passagem * 1.05
        cadastro_voo.append(desconto)    
        break    
    break 
while True:
   print("======CADASTRO AVIÃO======")

  

   while True:
      
        modelo = input("Informe o modelo do avião :")
        if modelo.isdigit():
          print("INVALIDO!")
        else:
         cadastro_voo.append(modelo)    
         break   
        
   while True:
        
        ano = int(input("Informe o ano do avião:"))
        if ano < 1990 and ano > 2030:
          print("INVALIDO!")
        else:
          cadastro_voo.append(ano)    
        break       
   while True:
        horas_de_voo = float(input("informe as horas de voo: "))   
        if horas_de_voo < 0 and horas_de_voo > 100:
            print("INVALIDO")
        else:
           cadastro_voo.append(horas_de_voo)
           break
   while True:
        cor = input("Informe a cor do avião :")
        if cor.isdigit():
          print("INVALIDO!")
        else:
         cadastro_voo.append(cor)    
         break   
   while True:
       qtnd_passageiros = int(input("informe a quamtidade de passageiros: "))   
       if qtnd_passageiros < 0 and qtnd_passageiros > 250:
            print("INVALIDO")
       else:
           cadastro_voo.append(qtnd_passageiros)
           break      
   break
while True:
    print("======CADASTRO TRIPULAÇÃO======")  

    while True:
        
    
        nome = input("Digite seu nome: ")
        if nome.isdigit():
            print(" INVALIDO!!! ")
        else:
            cadastro_tripulação.append(nome)    
        break
    while True:
        desc_cargo = input("Digite seu cargo: ")
        if desc_cargo.isdigit():
            print(" INVALIDO!!! ")
        else:
            cadastro_tripulação.append(desc_cargo) 
            break
    while True:
           idade = int(input("Digite sua idade: "))
           if   idade < 0 and idade > 120:
             print("Idade Invalida para embarcar")
           else:
            cadastro_tripulação.append(idade)
            break   
    while True:
        data_admissão = input("Data de Adimissão: ")
        if data_admissão.isdigit():
            print("INVALIDO")
        else:
            cadastro_tripulação.append(data_admissão)
            break
    while True:
         Tel = (input("informe seu telefone: "))
         if not Tel.isdigit() and len(Tel) < 10:
             print(" NUMERO DE TELEFONE INVALIDO ")
         else:
            cadastro_tripulação.append(Tel)
            break 
    break
while True:
    print("\n===================== RELATÓRIO COMPLETO =====================\n")

   
    print(">>> DADOS DO CLIENTE:")
    print(f"Nome completo       : {cadastro[0]} {cadastro[1]}")
    print(f"RG                  : {cadastro[2]}")
    print(f"CPF                 : {cadastro[3]}")
    print(f"Endereço            : {cadastro[4]}")
    print(f"Telefone            : {cadastro[5]}")
    print(f"Idade               : {cadastro[6]} anos")

 
    print("\n>>> DADOS DA PASSAGEM:")
    print(f"Destino             : {cadastro_voo[0]}")
    print(f"Origem              : {cadastro_voo[1]}")
    print(f"Duração do voo      : {cadastro_voo[2]} horas")
    print(f"Valor da passagem   : R$ {cadastro_voo[3]:.2f}")

    
    if cadastro_voo[3] > 2000:
        desconto = cadastro_voo[3] * 0.05
        valor_final = cadastro_voo[3] - desconto
        print(f"Desconto aplicado   : R$ {desconto:.2f} (5%)")
        print(f"Valor com desconto  : R$ {valor_final:.2f}")
    else:
        print("Desconto aplicado   : R$ 0.00")
        print(f"Valor com desconto  : R$ {cadastro_voo[3]:.2f}")

    print("\n>>> DADOS DO AVIÃO:")
    print(f"Modelo              : {cadastro_voo[5]}")
    print(f"Ano de fabricação   : {cadastro_voo[6]}")
    print(f"Horas de voo        : {cadastro_voo[7]}")
    print(f"Cor                 : {cadastro_voo[8]}")
    print(f"Capacidade (pax)    : {cadastro_voo[9]} passageiros")

    
    print("\n>>> DADOS DA TRIPULAÇÃO:")
    print(f"Nome do tripulante  : {cadastro_tripulação[0]}")
    print(f"Cargo               : {cadastro_tripulação[1]}")
    print(f"Idade               : {cadastro_tripulação[2]} anos")
    print(f"Data de admissão    : {cadastro_tripulação[3]}")
    print(f"Telefone            : {cadastro_tripulação[4]}")

    print("\n===================== FIM DO RELATÓRIO =====================")
    break

                

                 



            
