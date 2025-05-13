n = int(input("informe a quantidade de pessoas: " ))
media = 0
pessoas = []

for i in range(n):
    media += 1
    idade = int(input(f"idade de {media} pessoas: "))
    pessoas.append(idade)
media = sum(pessoas) / n

if idade > 0 and idade < 25:
    print("a turma é jovem!!")

elif idade > 26 and idade < 60:
    print("a turma é adulta!!")

elif idade > 60:
    print("a turma é idosa!!!")  

print("a media da idade das pessoas é: ", media)         
    