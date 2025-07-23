numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
numero3 = int(input("Digite o segundo numero: "))

if numero1 < numero2 and numero1 < numero3 and numero2 < numero3: # 1,2,3
    print((numero1), (numero2), (numero3))

elif numero1 < numero2 and numero1 < numero3 and numero3 < numero2: # 1, 3, 2  
    print(numero1, numero3, numero2)


elif numero2 < numero1 and numero2 < numero3 and numero1 < numero3: #2, 1, 3
 print((numero2), (numero1), (numero3))

elif numero2 < numero1 and numero2 < numero3 and numero3 < numero1:
    print(numero2, numero3, numero1 )
 

elif numero3 < numero1 and numero3 < numero2 and numero1 < numero2:
    print((numero3), (numero2), (numero1))   

elif numero3 < numero1 and numero3 < numero2 and numero2 < numero1:
   print(numero3, numero1, numero2)

    





