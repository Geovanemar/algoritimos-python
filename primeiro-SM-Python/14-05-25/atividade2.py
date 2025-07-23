dados = {"arroz": {"quantidade": 10, "valor": 35.99},
          "feijão": {"quantidade":2 , "valor": 29.99}, 
          "banana": {"quantidade":3, "valor": 6.99}, 
          "frango": {"quantidade": 15 , "valor": 20.00}, 
          "carne": {"quantidade": 11, "valor": 130.00}}

produtos = input("qual produto gostaria de saber o valor e quantidade?: ").lower()

if produtos in dados:
    print(dados [produtos])
else:
    print("ERRO!!!, PRODUTO NÃO ENCONTRADO")    

