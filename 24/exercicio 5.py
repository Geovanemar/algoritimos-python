while True:
    nome = input("Digite seu nome: ")
    idade = int(input("Digite a sua idade (0-150): "))
    salario = float(input("Digite seu salario: "))
    sexo = input("digite seu sexo: ").upper()
    estado_civil = input(" insira seu estado civil, S para solteiro, C para casado, V Para viuvo, D divorciado: ").upper()
    nome = input("Digite seu nome: ")
    if len(nome) < 3:
        print("nome invalido, seu nome precisa ter 3 ou mais caracteres ")
    else:
        break

    idade = int(input("Digite a sua idade (0-150): "))
    if idade > 150 and idade < 0:
        print("a sua idade não é valida ")
    else:
        break    
        
    salario = float(input("Digite seu salario: "))
    if salario < 0:
        print("seu salario não é valido ")
    else:
        break
    sexo = input("digite seu sexo: ").upper()
    if sexo != "f" and sexo != "m":
        print("seu sexo é valido")
    else:
        break    

    estado_civil = input(" insira seu estado civil, S para solteiro, C para casado, V Para viuvo, D divorciado: ").upper()
    if estado_civil == "s" and estado_civil == "c" and estado_civil == "v" and estado_civil == "d":
        print("seu estado civel é valido")
    else:
        break    

    print("nome", nome)                   
    print("idade", idade)                   
    print("salario", salario)                   
    print("sexo", sexo)                   
    print("estado civil", estado_civil)   
    break                
