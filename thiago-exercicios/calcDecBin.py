#Decimal para Binario
import os

valor = float(input("Digite um valor em decimal para converter em binario: "))
valor_binario = []

while valor > 0:
    novo_valor = valor % 2
    novo_valor = int(novo_valor)
    print("Resto: ", novo_valor)
    valor = valor / 2
    print("Divisor: ", valor)
    valor = int(valor)
    valor_binario.insert(0, novo_valor)

    print(valor_binario)
    print("".join(map(str, valor_binario)))











#decimal = []
#valor = 29

#novo_val = valor % 2

#print(novo_val)

#valor = valor / 2
#print(int(valor))
#decimal.insert(0,novo_val)

