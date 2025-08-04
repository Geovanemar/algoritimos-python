candidato_1 = 0
candidato_2 = 0
candidato_3 = 0
candidato_4 = 0
voto = 0
voto_nulo = 0
voto_branco = 0



while True:

    

    print("candidato_1 = 1, candidato_2 = 2, candidato_3 = 3, candidato_4 = 4, voto_nulo = 5, voto_branco = 6")
    voto = (input("informe seu voto: "))

    if voto == "1":
     candidato_1 += 1

    elif voto == "2":
     candidato_2 += 1

    elif voto == "3":
      candidato_3 += 1

    elif voto == "4":
      candidato_4 += 1  

    elif voto == "5":
      voto_nulo += 1

    elif voto == "":
      voto_branco += 1

    elif candidato_1 > candidato_2 and candidato_1 > candidato_3 and candidato_1 > candidato_4:
      print("cantidato 1 é o campeão")  

    elif candidato_2 > candidato_1 and candidato_2 > candidato_3 and candidato_2 > candidato_4:
      print("candidato 2 é o campeõa")  

    elif voto == "0":
      print("votos para canditado 1: ", candidato_1, "votos para candidato 2: ", candidato_2, "votos para candidato 3: ", candidato_3, "votos para candidato 4: ", candidato_4)
      break  

    else:
      print("esse numero não condiz ")


   

     

