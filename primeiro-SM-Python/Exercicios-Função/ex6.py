num = int(input("Digite um numero inteiro: "))

def fatorial(num):
    if num < 0:
        print("numero negativo não é valido")
    resultado = 1
    for i in range(1, num + 1):
        resultado = resultado *i
    print(resultado)

fatorial(num)        