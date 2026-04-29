import mysql.connector

# Criar conexão
conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "aula_connect"
)

def get_alunos():
    cursor = conexao.cursor()

    cursor.execute("select * from alunos: ")
    dados = cursor.fetchall()
     
    for aluno in dados:
        print(f"ID: {aluno[0]} Nome: {aluno[1]} Idade: {aluno[2]}")

    cursor.close()
    conexao.close()

get_alunos(
    
)        