import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, jsonify, request

from database import buscar_livros, buscar_por_id, listar_generos, listar_usuarios

app = Flask(__name__)
app.json.ensure_ascii = False  # mantém acentos legíveis no JSON


@app.route("/")
def home():
    return jsonify({
        "status": "sucesso",
        "mensagem": "Servidor da Livraria rodando com sucesso!",
        "endpoints_disponiveis": [
            "GET  /api/livros",
            "GET  /api/livros?genero=Fantasia",
            "GET  /api/livros/<id>",
            "GET  /api/generos",
            "GET  /api/usuarios",
        ],
    }), 200


@app.route("/api/livros", methods=["GET"])
def get_livros():
    genero =