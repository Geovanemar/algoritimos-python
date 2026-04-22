numero = int(input("Digite um número: "))

if numero % 2 == 0 and numero % 3 == 0 and numero % 5 == 0:
    print(f"O número {numero} é divisível por 2, 3 e 5.")
else:
    print(f"O número {numero} NÃO é divisível por 2, 3 e 5.")
