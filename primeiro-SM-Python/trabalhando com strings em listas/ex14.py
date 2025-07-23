lista = ["joana", "zoe", "ronaldo", "marcos", "sofia", "camilla" , "joao marcos ", "bruno mars"]

lista_filtrada2 = [lista for lista in lista  if len(lista) >= 6]

print(lista_filtrada2)