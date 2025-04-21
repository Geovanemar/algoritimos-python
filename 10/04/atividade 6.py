salario = float(input("Digite o salario:"))

if salario <= 280.55:
    aumento1 = (salario * 0.2251)
    salario_final = salario + aumento1
    print("primeiro salario é: ",salario, "com aumento" , aumento1, "salario final: " , salario_final)

elif salario >= 280.55 and salario <= 709.72:
    aumento2 = (salario * 0.1539) 
    salario_final = salario + aumento2
    print("primeiro salario é: ", salario, "com aumento" , aumento2, "salario final: " , salario_final)
elif salario >= 709.72 and salario <= 1501.33:
    aumento3 = (salario * 0.1097)  
    salario_final = (salario + aumento3)
    print("primeiro salario é: ", salario , "com aumento: ", aumento3, "salario final: " , salario_final )  
    
elif salario >= 1501.33:
    aumento4 = (salario * 0.519)
    salario_final = (salario + aumento4)
    print("primeiro salario: ", salario, "com aumento: ", aumento4, "salario final: " , salario_final)    