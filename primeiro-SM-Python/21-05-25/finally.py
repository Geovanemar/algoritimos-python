try:
   a = int(input("digite uma palavra: "))
except ValueError:
   print("Digite apenas numeros")
except:
   print("Erro desconhecido")     
finally:
   print("final do algortimo")   