class Calculadora:
        pass
        def calcular(self,opcao,num1,num2):
            if opcao == "+":
                return self.__adicionar(num1,num2)
            elif opcao == "-":
                return self.__subtrair(num1,num2)
            else:
                print("Opção invalida")

        def __adicionar(self,n1,n2):
            return n1 + n2

        def __subtrair(self,n1,n2):
            return n1 + n2

calc = Calculadora()
resultado = calc.calcular("-", 100, 40)
print(resultado)