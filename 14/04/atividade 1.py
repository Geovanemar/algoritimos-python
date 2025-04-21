nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a primeira nota: "))

media = (nota1 + nota2)/2

if media >= 7 and media <= 9.9:
    print("Aprovado!!!")

elif media <= 6:
    print("Reprovado")

elif media == 10:
    print("Aprovado com distinção")    

    