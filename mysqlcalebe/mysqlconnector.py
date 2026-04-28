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
 
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS alunos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) not null,
    idade int not null)
    """)
 
#comando insert para adicionar um aluno
 
sql = "INSERT INTO alunos (nome, idade) VALUES (%s, %s)"
 
valores = ("João", 20)
cursor.execute(sql, valores)
 
#executar consulta para mostrar os alunos
 
cursor.execute("SELECT * FROM alunos")
resultados = cursor.fetchall()
for linha in resultados:
    print(linha)
 
#fechar a conexao
cursor.close()
conexao.close()
 