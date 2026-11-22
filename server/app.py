import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, jsonify, request

from database import buscar_livros, buscar_por_id, listar_generos

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
        ],
    }), 200


@app.route("/api/livros", methods=["GET"])
def get_livros():
    genero = request.args.get("genero")
    return jsonify({"status": "sucesso", "dados": buscar_livros(genero)}), 200


@app.route("/api/livros/<int:livro_id>", methods=["GET"])
def get_livro(livro_id):
    livro = buscar_por_id(livro_id)
    if livro is None:
        return jsonify({"status": "erro", "mensagem": "Livro não encontrado"}), 404
    return jsonify({"status": "sucesso", "dados": livro}), 200


@app.route("/api/generos", methods=["GET"])
def get_generos():
    return jsonify({"status": "sucesso", "dados": listar_generos()}), 200


if __name__ == "__main__":
    app.run(port=5000, debug=True)
