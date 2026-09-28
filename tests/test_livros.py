import pytest

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


def test_busca_por_titulo_ou_autor_ignora_maiusculas_e_minusculas():
    service = LivroService()

    resultados = service.buscar_por_titulo_ou_autor("MACHADO")

    assert {livro.id for livro in resultados} == {1, 8}


def test_filtro_de_acessibilidade_combina_recursos_com_and():
    service = LivroService()

    resultados = service.filtrar_por_acessibilidade(["audiolivro", "compatibilidade_leitor_tela"])

    assert [livro.id for livro in resultados] == [1, 5, 8]


def test_filtro_sem_resultados_retorna_lista_vazia():
    service = LivroService()

    service.excluir_livro(8)

    assert service.filtrar_por_acessibilidade(
        ["braille", "fonte_ampliada", "compatibilidade_leitor_tela"]
    ) == []


def test_busca_vazia_e_recurso_desconhecido_sao_rejeitados():
    service = LivroService()

    with pytest.raises(ValueError):
        service.buscar_por_titulo_ou_autor("  ")
    with pytest.raises(ValueError):
        service.filtrar_por_acessibilidade(["recurso_inexistente"])


def test_atualizar_livro_preserva_recursos_nao_informados():
    service = LivroService()

    atualizado = service.atualizar_livro(1, "Dom Casmurro - edição", "Machado de Assis", 1899)

    assert atualizado is not None
    assert atualizado.titulo == "Dom Casmurro - edição"
    assert atualizado.audiolivro is True
    assert service.buscar_por_id(1) == atualizado


def test_atualizacao_invalida_nao_modifica_livro_existente():
    service = LivroService()
    original = service.buscar_por_id(1)

    with pytest.raises(ValueError):
        service.atualizar_livro(1, "  ", "Machado de Assis", 1899)

    assert service.buscar_por_id(1) is original


def test_excluir_livro_remove_existente_e_indica_id_inexistente():
    service = LivroService()

    assert service.excluir_livro(1) is True
    assert service.buscar_por_id(1) is None
    assert service.excluir_livro(9999) is False


@pytest.mark.parametrize(
    "dados",
    [
        {"titulo": "  ", "autor": "Autor", "ano_publicacao": 2000},
        {"titulo": "Título", "autor": "  ", "ano_publicacao": 2000},
        {"titulo": "Título", "autor": "Autor", "ano_publicacao": "2000"},
    ],
)
def test_livro_rejeita_dados_obrigatorios_invalidos(dados):
    with pytest.raises(ValueError):
        Livro(id=1, **dados)


@pytest.mark.parametrize("campo, valor", [("id", 0), ("audiolivro", "sim")])
def test_livro_rejeita_id_ou_recurso_com_tipo_invalido(campo, valor):
    dados = {
        "id": 1,
        "titulo": "Título",
        "autor": "Autor",
        "ano_publicacao": 2000,
    }
    dados[campo] = valor

    with pytest.raises(ValueError):
        Livro(**dados)


def test_livro_com_ano_publicacao_invalido_gera_erro():
    with pytest.raises(ValueError):
        Livro(id=1, titulo="Titulo", autor="Autor", ano_publicacao=0)
