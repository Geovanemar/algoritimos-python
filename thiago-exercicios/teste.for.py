i = 0
j = 0

matriz = []
lin = int(input("Digite a quantidade de linhas: "))
col = int(input("Digite a quantidade de colunas: "))

while i < lin:
    linha = []
    while j < col:
        num = 1
        linha.append(num)
        j = j + 1
    matriz.append(linha) 
    i = i + 1
    j = 0

print(matriz)   

