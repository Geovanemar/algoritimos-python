while True:
   valor =(input("Digite M pra multiplicação, S para subtração, A para adição, D para divisão, X para sair: ")).upper()

   if valor == "M":
      X = float(input("digite um numero:"))
      Y = float(input("digite outro numero:"))

      Z = X * Y
      print("o valor é igual a: " , Z)

   if valor == "S":
      X = float(input("digite um numero:"))
      Y = float(input("digite outro numero:"))

      Z = X - Y
      print("o valor é igual a: " , Z) 

   if valor == "A":
      X = float(input("digite um numero:"))
      Y = float(input("digite outro numero:"))

      Z = X + Y
      print("o valor é igual a: " , Z)  

       
   if valor == "D":
      X = float(input("digite um numero:"))
      Y = float(input("digite outro numero:"))

      Z = X / Y
      print("o valor é igual a: " , Z)