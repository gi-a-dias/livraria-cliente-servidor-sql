
from config import colecao_livros


def buscar_livros(genero=None):
    filtro = {}
    if genero:
        filtro["genero"] = {"$regex": f"^{genero}$", "$options": "i"}

    livros = list(colecao_livros.find(filtro, {"_id": 0}))
    return livros


def buscar_por_id(livro_id):
    return colecao_livros.find_one({"id": livro_id}, {"_id": 0})


def listar_generos():
    return sorted(colecao_livros.distinct("genero"))
