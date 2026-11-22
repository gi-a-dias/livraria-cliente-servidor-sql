
from config import client, colecao_livros

try:
    client.admin.command("ping")
    print("Conexão com o Azure DocumentDB realizada com sucesso!")

    print("Nome da coleção:", colecao_livros.name)
    print("Quantidade de livros cadastrados:", colecao_livros.count_documents({}))

except Exception as erro:
    print("Erro ao conectar:", erro)

finally:
    client.close()
