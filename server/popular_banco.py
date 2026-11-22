
from config import colecao_livros

LIVROS = [
    {"id": 1, "titulo": "O Hobbit", "autor": "J.R.R. Tolkien", "genero": "Fantasia", "preco": 45.0, "estoque": 3},
    {"id": 2, "titulo": "1984", "autor": "George Orwell", "genero": "Ficção", "preco": 30.0, "estoque": 5},
    {"id": 3, "titulo": "Senhor dos Anéis", "autor": "J.R.R. Tolkien", "genero": "Fantasia", "preco": 60.0, "estoque": 1},
    {"id": 4, "titulo": "Dom Casmurro", "autor": "Machado de Assis", "genero": "Romance", "preco": 35.0, "estoque": 4},
    {"id": 5, "titulo": "A Revolução dos Bichos", "autor": "George Orwell", "genero": "Ficção", "preco": 28.0, "estoque": 6},
    {"id": 6, "titulo": "Harry Potter e a Pedra Filosofal", "autor": "J.K. Rowling", "genero": "Fantasia", "preco": 40.0, "estoque": 7},
    {"id": 7, "titulo": "O Pequeno Príncipe", "autor": "Antoine de Saint-Exupéry", "genero": "Infantil", "preco": 25.0, "estoque": 8},
    {"id": 8, "titulo": "Capitães da Areia", "autor": "Jorge Amado", "genero": "Romance", "preco": 32.0, "estoque": 2},
    {"id": 9, "titulo": "Duna", "autor": "Frank Herbert", "genero": "Ficção Científica", "preco": 50.0, "estoque": 3},
    {"id": 10, "titulo": "A Metamorfose", "autor": "Franz Kafka", "genero": "Ficção", "preco": 29.0, "estoque": 5}
]

for livro in LIVROS:
    colecao_livros.update_one(
        {"id": livro["id"]},
        {"$set": livro},
        upsert=True
    )

print(f"{colecao_livros.count_documents({})} livros cadastrados no banco!")
