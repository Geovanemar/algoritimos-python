import mysql.connector
from db import conectar
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/alunos", methods = ["GET"])
def get_alunos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("select * from alunos")
    dados = cursor.fetchall()

    alunos = []
    for aluno in dados:
        alunos.append({
                "id": aluno[0],
                "nome": aluno[1],
                "idade": aluno[2]
            })
        #print(f"ID: {aluno[0]} | Nome: {aluno[1]} | Idade: {aluno[2]}")
    
    cursor.close()
    conexao.close()

    return jsonify(alunos)

@app.route("/alunos", methods=["POST"])
def post_aluno():

    dados = request.json

    nome = dados["nome"]
    idade = dados["idade"]

    conexao = conectar()
    cursor = conexao.cursor()

    sql = "INSERT INTO alunos(nome, idade) VALUES (%s, %s)"
    cursor.execute(sql, (nome, idade))

    conexao.commit()

    cursor.close()
    conexao.close()

    return jsonify({"mensagem": "Aluno adicionado com sucesso"})


@app.route("/alunos/<int:id>", methods=["PUT"])
def put_aluno_api(id):

    dados = request.json

    nome = dados["nome"]
    idade = dados["idade"]

    conexao = conectar()
    cursor = conexao.cursor()

    sql = "UPDATE alunos SET nome=%s, idade=%s WHERE id=%s"
    cursor.execute(sql, (nome, idade, id))

    conexao.commit()

    cursor.close()
    conexao.close()

    return jsonify({"mensagem": "Aluno atualizado"})

@app.route("/alunos/<int:id>", methods=["DELETE"])
def delete_aluno_api(id):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = "DELETE FROM alunos WHERE id=%s"
    cursor.execute(sql, (id,))

    conexao.commit()

    cursor.close()
    conexao.close()

    return jsonify({"mensagem": "Aluno deletado com sucesso"})


if __name__ == "__main__":
    app.run(debug=True)