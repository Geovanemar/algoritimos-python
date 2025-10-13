import random


class Robo:
    def __init__(self, identificador, nome, energia, nivel):
        self.identificador = identificador
        self.nome = nome
        self.energia = energia
        self.nivel = nivel

    def __str__(self):
        return f"ID: {self.identificador} | Nome: {self.nome} | Energia: {self.energia} | Nível: {self.nivel}"



base = []           
campo = [[0, 0],    
         [0, 0]]


def cadastrar_robo():
    if len(base) >= 4:
        print("❌ Limite de 4 robôs atingido!")
        return
    
    identificador = len(base) + 1
    nome = input("Digite o nome do robô: ")
    energia = int(input("Digite a energia do robô: "))
    nivel = int(input("Digite o nível do robô: "))

    robo = Robo(identificador, nome, energia, nivel)
    base.append(robo)
    print("✅ Robô cadastrado com sucesso!")


def listar_robos():
    if not base:
        print("Nenhum robô cadastrado.")
    else:
        for robo in base:
            print(robo)


def mostrar_campo():
    print("\n=== Campo de Missão ===")
    for linha in campo:
        print(linha)
    print("=======================\n")


def simular_missao():
    if not base:
        print("Não há robôs na base para missão.")
        return

    listar_robos()
    escolha = int(input("Escolha o ID do robô para a missão: "))
    robo = next((r for r in base if r.identificador == escolha), None)

    if not robo:
        print("Robô não encontrado!")
        return

    if robo.energia > 20:
        print(f"✅ Missão do robô {robo.nome} foi um sucesso!")
        robo.energia -= 20

       
        base.remove(robo)

        
        while True:
            i, j = random.randint(0, 1), random.randint(0, 1)
            if campo[i][j] == 0:
                campo[i][j] = robo.identificador
                break
    else:
        print(f"❌ Missão do robô {robo.nome} falhou (energia insuficiente).")


def recuperar_robo():
    mostrar_campo()
    id_robo = int(input("Digite o ID do robô que deseja recuperar: "))

    encontrado = False
    for i in range(2):
        for j in range(2):
            if campo[i][j] == id_robo:
                campo[i][j] = 0
                
                nome = input("Digite novamente o nome do robô recuperado: ")
                energia = int(input("Digite a energia atual do robô: "))
                nivel = int(input("Digite o nível do robô: "))
                robo = Robo(id_robo, nome, energia, nivel)
                base.append(robo)
                print(f"🔄 Robô {nome} recuperado com sucesso para a base!")
                encontrado = True
                break
    if not encontrado:
        print("❌ Robô não encontrado no campo de missão.")



def menu():
    while True:
        print("\n=== MENU ===")
        print("1 - Cadastrar robô")
        print("2 - Listar robôs")
        print("3 - Simular missão")
        print("4 - Mostrar campo de missão")
        print("5 - Recuperar robô")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_robo()
        elif opcao == "2":
            listar_robos()
        elif opcao == "3":
            simular_missao()
        elif opcao == "4":
            mostrar_campo()
        elif opcao == "5":
            recuperar_robo()
        elif opcao == "6":
            print("Encerrando o sistema...")
            break
        else:
            print("❌ Opção inválida!")



menu()
