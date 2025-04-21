num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

diferenca = abs(num1 - num2)  
if diferenca > 20:
    print("A diferença entre os números é maior que 20.")
else:
    print("A diferença entre os números NÃO é maior que 20.")
