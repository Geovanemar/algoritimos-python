f = open("file.txt" , "r") # r, read(), ler o que esta dentro do arquivo
print(f.read())
f.close()


f = open("file.txt" , "a" , encoding="utf-8")
f.write("\nadicionando conteúdo!") #como se fosse o append para adicionar
f = open("file.txt" , "r")
print(f.read)