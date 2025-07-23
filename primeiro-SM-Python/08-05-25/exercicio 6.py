n = 0
valor = 0
soma = float("-inf")
menor = float("inf")
maior = 0

qtnd = int(input("Digite os numeros: "))

for i in range(qtnd):
    print(f"Digite: {i+1} º numero")
    valor = int(input())
    soma = soma + i


    if valor > maior:
        maior = valor
    
    elif valor < menor:
         menor = valor

print("o maior:  {maior}")
print("o menor, {menor}")
print("a soma é:  {soma}")      
            

