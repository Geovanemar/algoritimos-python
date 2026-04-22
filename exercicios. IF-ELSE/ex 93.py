num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

soma = num1 + num2

if soma > 50 and soma % 3 == 0:
    print(f"A soma soma é maior que 50 e é múltiplo de 3.")
else:
    print(f"A soma soma NÃO atende os dois critérios.")
