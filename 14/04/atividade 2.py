
valor_hora = float(input("Digite o valor das horas trabalhadas:"))
horas_trabalhadas = int(input("Digite as horas trabalhadas: "))

salariobruto = horas_trabalhadas * valor_hora
fgts = salariobruto * 0.11
INSS = salariobruto * 0.1

if salariobruto <= 900:
    
    print("salario bruto: " , salariobruto * valor_hora)
    print("(-) IR ISENTO" )               
    print("iNSS" "10%" , INSS) 
    print("FGTS" "5%" , fgts )
    print("total de desconto: " , INSS)
    print("salario liquido: " , salariobruto)

elif salariobruto >= 900 and salariobruto <= 1500:

    IR5 = (salariobruto * 0.05)
    desconto = (IR5 + INSS)
    print("salario bruto: " , salariobruto )
    print("(-) IR " , IR5 )               
    print("iNSS" "10%" , INSS) 
    print("FGTS" "5%" , fgts )
    print("total de desconto: " , desconto)
    print("salario liquido: " , salariobruto)

elif salariobruto >= 1500 and salariobruto <= 2500:
    IR10 = (salariobruto * 0.1)
    desconto2 = (IR10 + INSS)
    print("salario bruto: " , salariobruto )
    print("(-) IR " , IR10)               
    print("iNSS" "10%" , INSS) 
    print("FGTS" "5%" , fgts )
    print("total de desconto: " , desconto2)
    print("salario liquido: " , desconto2)

elif salariobruto > 2500:
    IR20 = (salariobruto * 0.20)
    desconto3 = (IR20 + INSS)
    print("salario bruto: " , salariobruto)
    print("(-) IR " , IR20 )               
    print("iNSS" "10%" , INSS) 
    print("FGTS" "5%" , fgts )
    print("total de desconto: " , desconto3)
    print("salario liquido: " , desconto3)