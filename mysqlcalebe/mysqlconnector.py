import mysql.connector
 
#criar uma conexao com o banco de dados
 
conexao = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
)
 
if conexao.is_connected():
    print("Conexão bem sucedida!")
 
#criar um cursor para executar comandos SQL
 
cursor = conexao.cursor()
 
cursor.execute("CREATE DATABASE IF NOT EXISTS aula_connector")
 
conexao.database = "aula_connector"
 
cursor.execute("show databases")
 
#mostrar os bancos de dados existentes
 
for banco in cursor.fetchall():
    print(banco)

cursor.execute()
('''
    CREATE TABLE IF NOTS EXITS alunos(
    id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(100) not null,
    idade int not null) 
  ''')    

sql = "INSERT INTO alunos (nome, idade) VALUES (%s, %s)"

valores =