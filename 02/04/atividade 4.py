salario = float(input("Digite seu salario: "))

if salario < 500: 
    print("reajuste de 15%")
    total = salario + (salario * 15 / 100)

elif salario >= 500 and salario <= 1000:
    print("reajuste de 10% ")
    total = salario + (salario * 10 / 100)

elif salario > 1000:
    print("reajuste de 5% ")
    total = salario + (salario * 10 / 100)
    print(total)





