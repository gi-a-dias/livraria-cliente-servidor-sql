from config import get_connection


def _consultar(sql, params=None, um=False):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(sql, params)
            return cur.fetchone() if um else cur.fetchall()
    finally:
        conn.close()


def buscar_livros(genero=None):
    base = ("SELECT id, titulo, autor, genero, preco::float AS preco, estoque "
            "FROM livros")
    if genero:
        sql = base + " WHERE LOWER(genero) = LOWER(%s) ORDER BY id"
        return [dict(r) for r in _consultar(sql, (genero,))]
    return [dict(r) for r in _consultar(base + " ORDER BY id")]


def buscar_por_id(livro_id):
    sql = ("SELECT id, titulo, autor, genero, preco::float AS preco, estoque "
           "FROM livros WHERE id = %s")
    r = _consultar(sql, (livro_id,), um=True)
    return dict(r) if r else None


def listar_generos():
    rows = _consultar("SELECT DISTINCT genero FROM livros ORDER BY genero")
    return [r["genero"] for r in rows]


def listar_usuarios():
    sql = ("SELECT id, nome, email, telefone, criado_em::text AS criado_em "
           "FROM usuarios ORDER BY id")
    return [dict(r) for r in _consultar(sql)]