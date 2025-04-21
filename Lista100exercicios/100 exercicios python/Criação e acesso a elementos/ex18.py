#Crie uma lista e rotacione seus elementos uma posição à direita.

lista = [23, 34, 56, 98, 65]

listarotacionada = [lista [-1]] + lista[:-1]
print(listarotacionada)