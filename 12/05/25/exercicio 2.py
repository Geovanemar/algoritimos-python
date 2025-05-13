n = int(input("numero total de eleitores: ")) 
cont = 0
n_votos = 0
cand1 = 0
cand2 = 0
cand3 = 0
for i in range(n):
    cont += 1
    
    n_votos = int(input(f" Eleitor {cont}: 1 para votar em  can1, 2 para votar em  cand2, 3 para votar em cand3: "))
    
    if n_votos == 1:
         cand1 += 1

    elif n_votos == 2:
        cand2 += 1

    elif n_votos == 3:
        cand3  += 1  

print("a votação terminou!!")

print(" canditado 1: ", cand1 , "votos")
print(" canditado 2: ", cand2 , "votos")
print(" canditado 3: ", cand3 , "votos")

if cand1 > cand2 and cand1 > cand3:
    print("o candidado 1 foi o campeão!!")

elif cand2 > cand1 and cand2 > cand3:
    print("o candidato 2 foi o campeão!!!")

elif cand3 > cand1 and cand3 > cand2:
    print("candidato 3 foi o campeão!!!")     

else:
    print(f"houve um empate, aguarde a segundo turno")       




    
    




