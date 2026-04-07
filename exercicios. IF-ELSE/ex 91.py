num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

soma = num1 + num2

if soma > 100 and soma % 10 == 0:
    print(f"A soma ({soma}) é maior que 100 e é múltiplo de 10.")
else:
    print(f"A soma ({soma}) NÃO atende os dois critérios.")
