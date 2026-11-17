import os
import pymysql
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for

load_dotenv()
app = Flask(__name__)


def conectar_bd():
    return pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=int(os.getenv("DB_PORT", 3306)),
        database=os.getenv("DB_NAME"),
        cursorclass=pymysql.cursors.DictCursor,
        connect_timeout=5
    )


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


@app.route("/contato", methods=["GET", "POST"])
def contato():
    if request.method == "POST":
        nome = request.form["nome"]
        curso = request.form["curso"]
        email = request.form["email"]

        conexao = conectar_bd()
        try:
            with conexao.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO alunos (nome, curso, email) VALUES (%s, %s, %s)",
                    (nome, curso, email)
                )
            conexao.commit()
        finally:
            conexao.close()

        return redirect(url_for("listar"))

    return render_template("cadastro.html")


@app.route("/listar")
def listar():
    conexao = conectar_bd()
    try:
        with conexao.cursor() as cursor:
            cursor.execute("SELECT * FROM alunos")
            alunos = cursor.fetchall()
    finally:
        conexao.close()
    return render_template("listar.html", alunos=alunos)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
