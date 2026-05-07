import mysql.connector

def conectar():

    conexao = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="aula connect"
    )

    return conexao

import mysql.connector
from db import conectar
 
from flask import Flask, request, jsonify
 
app = Flask(__name__)
 
@app.route('/alunos', methods=['GET'])
 
def get_alunos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM alunos")
    dados = cursor.fetchall()
   
    for aluno in dados:
        print(f"ID: {aluno[0]}, Nome: {aluno[1]}, Idade: {aluno[2]} ")
 
    cursor.close()
    conexao.close()
 
def post_aluno():
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
 
    conexao = conectar()
    cursor = conexao.cursor()
 
    sql = "INSERT INTO alunos (nome, idade) VALUES (%s, %s)"
    cursor.execute(sql, (nome, idade))
    conexao.commit()
 
    print("Aluno cadastrado com sucesso!")
 
    cursor.close()
    conexao.close()
 
if __name__ == '__main__':
    app.run(debug=True)
 