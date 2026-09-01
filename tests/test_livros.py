from models.livro import Livro
from services.livro_service import LivroService


def test_lista_inicial_possui_dez_livros():
    service = LivroService()
    assert len(service.listar_livros()) == 10


def test_recursos_disponiveis_retorna_apenas_recursos_marcados():
    livro = Livro(id=1, titulo="Titulo", autor="Autor", ano_publicacao=2000, audiolivro=True)
    assert livro.recursos_disponiveis() == ["Audiolivro"]


def test_recursos_disponiveis_vazio_quando_nenhum_recurso():
    livro = Livro(id=1, titulo="Titulo", autor="Autor", ano_publicacao=2000)
    assert livro.recursos_disponiveis() == []


def test_cadastrar_livro_adiciona_na_lista():
    service = LivroService()
    total_antes = len(service.listar_livros())

    novo = service.cadastrar_livro(
        titulo="Novo Livro",
        autor="Novo Autor",
        ano_publicacao=2024,
        audiolivro=True,
    )

    assert len(service.listar_livros()) == total_antes + 1
    assert novo.audiolivro is True
    assert "Audiolivro" in novo.recursos_disponiveis()


def test_cadastrar_livro_gera_id_incremental():
    service = LivroService()
    ultimo_id = service.listar_livros()[-1].id

    novo = service.cadastrar_livro(titulo="X", autor="Y", ano_publicacao=2020)

    assert novo.id == ultimo_id + 1


def test_buscar_por_id_encontra_livro_existente():
    service = LivroService()
    livro = service.buscar_por_id(1)

    assert livro is not None
    assert livro.id == 1


def test_buscar_por_id_retorna_none_quando_nao_existe():
    service = LivroService()
    assert service.buscar_por_id(9999) is None
