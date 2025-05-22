while True:
   valor =(input("Digite M pra multiplicação, S para subtração, A para adição, D para divisão, X para sair: ")).upper()
   if valor == "X":
     break
   
   elif valor == "M":
      X = float(input("digite um numero:"))
      Y = float(input("digite outro numero:"))
     
      Z = X * Y
      print("o valor é igual a: " , Z)

   elif valor == "S":
      X = float(input("digite um numero:"))
      Y = float(input("digite outro numero:"))

      Z = X - Y
      print("o valor é igual a: " , Z) 

   elif valor == "A":
      X = float(input("digite um numero:"))
      Y = float(input("digite outro numero:"))

      Z = X + Y
      print("o valor é igual a: " , Z)  

       
   elif valor == "D":
      X = float(input("digite um numero:"))
      Y = float(input("digite outro numero:"))

      Z = X / Y
      print("o valor é igual a: " , Z)
