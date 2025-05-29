with open("cadastro.txt","r") as f:
    for linha in f:
        print(linha)
        if "joao" in linha.lower():
            print(linha)
            