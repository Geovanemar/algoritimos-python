num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

diferenca = abs(num1 - num2)  
if diferenca < 10:
    print("A diferença entre os números é menor que 10.")
else:
    print("A diferença entre os números NÃO é menor que 10.")
