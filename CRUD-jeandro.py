import mysql.connector
from mysql.connector import Error

class CRUDUsuario:
    def __init__(self, host='localhost', user='root', password='', database='db_usuario'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conexao = None
    
    def conectar(self):
        try:
            self.conexao = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.conexao.is_connected():
                print("Conexão com banco de dados estabelecida com sucesso!")
                return True
        except Error as erro:
            print(f"Erro ao conectar ao banco de dados: {erro}")
            return False
    
    def desconectar(self):
        if self.conexao and self.conexao.is_connected():
            self.conexao.close()
            print("Conexão fechada com sucesso!")
    
    def criar_usuario(self, nome, email, endereco=''):
        try:
            cursor = self.conexao.cursor()
            sql = "INSERT INTO usuarios (nome, email, endereco) VALUES (%s, %s, %s)"
            valores = (nome, email, endereco)
            cursor.execute(sql, valores)
            self.conexao.commit()
            print(f"Usuário '{nome}' criado com sucesso!")
            return True
        except Error as erro:
            print(f"Erro ao criar usuário: {erro}")
            return False
        finally:
            cursor.close()
    
    def ler_usuarios(self):
        try:
            cursor = self.conexao.cursor()
            sql = "SELECT id, nome, email, endereco FROM usuarios"
            cursor.execute(sql)
            usuarios = cursor.fetchall()
            
            if usuarios:
                print("\n=== LISTA DE USUÁRIOS ===")
                for usuario in usuarios:
                    print(f"ID: {usuario[0]}")
                    print(f"Nome: {usuario[1]}")
                    print(f"Email: {usuario[2]}")
                    print(f"Endereço: {usuario[3]}")
                    print("-" * 40)
                return usuarios
            else:
                print("Nenhum usuário encontrado!")
                return []
        except Error as erro:
            print(f"Erro ao ler usuários: {erro}")
            return []
        finally:
            cursor.close()
    
    def ler_usuario_por_id(self, usuario_id):
        try:
            cursor = self.conexao.cursor()
            sql = "SELECT id, nome, email, endereco FROM usuarios WHERE id = %s"
            cursor.execute(sql, (usuario_id,))
            usuario = cursor.fetchone()
            
            if usuario:
                print("\n=== DADOS DO USUÁRIO ===")
                print(f"ID: {usuario[0]}")
                print(f"Nome: {usuario[1]}")
                print(f"Email: {usuario[2]}")
                print(f"Endereço: {usuario[3]}")
                return usuario
            else:
                print(f"Usuário com ID {usuario_id} não encontrado!")
                return None
        except Error as erro:
            print(f"Erro ao ler usuário: {erro}")
            return None
        finally:
            cursor.close()
    
    def atualizar_usuario(self, usuario_id, nome=None, email=None, endereco=None):
        try:
            cursor = self.conexao.cursor()
            
            usuario = self.ler_usuario_por_id(usuario_id)
            if not usuario:
                return False
            
            nome = nome if nome else usuario[1]
            email = email if email else usuario[2]
            endereco = endereco if endereco else usuario[3]
            
            sql = "UPDATE usuarios SET nome = %s, email = %s, endereco = %s WHERE id = %s"
            valores = (nome, email, endereco, usuario_id)
            cursor.execute(sql, valores)
            self.conexao.commit()
            
            print(f"Usuário ID {usuario_id} atualizado com sucesso!")
            return True
        except Error as erro:
            print(f"Erro ao atualizar usuário: {erro}")
            return False
        finally:
            cursor.close()
    
    def deletar_usuario(self, usuario_id):
        try:
            cursor = self.conexao.cursor()
            
            usuario = self.ler_usuario_por_id(usuario_id)
            if not usuario:
                return False
            
            sql = "DELETE FROM usuarios WHERE id = %s"
            cursor.execute(sql, (usuario_id,))
            self.conexao.commit()
            
            print(f"Usuário ID {usuario_id} deletado com sucesso!")
            return True
        except Error as erro:
            print(f"Erro ao deletar usuário: {erro}")
            return False
        finally:
            cursor.close()


def criar_banco_e_tabela():
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''
        )
        cursor = conexao.cursor()
        
        cursor.execute("CREATE DATABASE IF NOT EXISTS db_usuario")
        print("Banco de dados 'db_usuario' criado ou já existe!")
        
        cursor.execute("USE db_usuario")
        
        sql_tabela = """
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            endereco VARCHAR(255),
            data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        cursor.execute(sql_tabela)
        print("Tabela 'usuarios' criada ou já existe!")
        
        conexao.commit()
        cursor.close()
        conexao.close()
        return True
    except Error as erro:
        print(f"Erro ao criar banco e tabela: {erro}")
        return False


def menu_principal():
    print("\n=== SISTEMA CRUD DE USUÁRIOS ===")
    print("1. Criar novo usuário")
    print("2. Listar todos os usuários")
    print("3. Buscar usuário por ID")
    print("4. Atualizar usuário")
    print("5. Deletar usuário")
    print("6. Sair")
    print("=" * 35)


def main():
    criar_banco_e_tabela()
    
    crud = CRUDUsuario()
    
    if not crud.conectar():
        print("Não foi possível conectar ao banco de dados!")
        return
    
    while True:
        menu_principal()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            nome = input("Digite o nome do usuário: ")
            email = input("Digite o email do usuário: ")
            endereco = input("Digite o endereço do usuário (opcional): ")
            crud.criar_usuario(nome, email, endereco)
        
        elif opcao == '2':
            crud.ler_usuarios()
        
        elif opcao == '3':
            usuario_id = int(input("Digite o ID do usuário: "))
            crud.ler_usuario_por_id(usuario_id)
        
        elif opcao == '4':
            usuario_id = int(input("Digite o ID do usuário a atualizar: "))
            nome = input("Digite o novo nome (deixe em branco para manter): ")
            email = input("Digite o novo email (deixe em branco para manter): ")
            endereco = input("Digite o novo endereço (deixe em branco para manter): ")
            
            nome = nome if nome else None
            email = email if email else None
            endereco = endereco if endereco else None
            
            crud.atualizar_usuario(usuario_id, nome, email, endereco)
        
        elif opcao == '5':
            usuario_id = int(input("Digite o ID do usuário a deletar: "))
            confirmacao = input("Tem certeza que deseja deletar? (s/n): ")
            if confirmacao.lower() == 's':
                crud.deletar_usuario(usuario_id)
        
        elif opcao == '6':
            print("Encerrando o programa...")
            break
        
        else:
            print("Opção inválida! Tente novamente.")
    
    crud.desconectar()


if __name__ == "__main__":
    main()