import os

import requests
from flask import Flask, jsonify, render_template, request

SERVER_URL = os.environ.get("SERVER_URL", "http://127.0.0.1:5000")

app = Flask(__name__)


def chamar_servidor(caminho, params=None):
    """Faz a requisição ao servidor e devolve (json, status_http)."""
    try:
        resp = requests.get(f"{SERVER_URL}{caminho}", params=params, timeout=5)
        return resp.json(), resp.status_code
    except requests.exceptions.RequestException:
        return {
            "status": "erro",
            "mensagem": "Não consegui falar com o servidor. Ele está rodando na porta 5000?",
        }, 503


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/livros")
def livros():
    dados, status = chamar_servidor("/api/livros", {"genero": request.args.get("genero")})
    return jsonify(dados), status


@app.route("/api/generos")
def generos():
    dados, status = chamar_servidor("/api/generos")
    return jsonify(dados), status


if __name__ == "__main__":
    app.run(port=5001, debug=True)
