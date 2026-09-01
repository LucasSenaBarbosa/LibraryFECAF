from typing import List, Optional

from data.livros import livros_iniciais
from models.livro import Livro


class LivroService:
    """Gerencia o catálogo de livros: listagem e cadastro de novas obras."""

    def __init__(self) -> None:
        self._livros: List[Livro] = livros_iniciais()

    def listar_livros(self) -> List[Livro]:
        return list(self._livros)

    def buscar_por_id(self, livro_id: int) -> Optional[Livro]:
        return next((livro for livro in self._livros if livro.id == livro_id), None)

    def _proximo_id(self) -> int:
        if not self._livros:
            return 1
        return max(livro.id for livro in self._livros) + 1

    def cadastrar_livro(
        self,
        titulo: str,
        autor: str,
        ano_publicacao: int,
        audiolivro: bool = False,
        braille: bool = False,
        ebook_acessivel: bool = False,
        fonte_ampliada: bool = False,
        compatibilidade_leitor_tela: bool = False,
    ) -> Livro:
        novo_livro = Livro(
            id=self._proximo_id(),
            titulo=titulo,
            autor=autor,
            ano_publicacao=ano_publicacao,
            audiolivro=audiolivro,
            braille=braille,
            ebook_acessivel=ebook_acessivel,
            fonte_ampliada=fonte_ampliada,
            compatibilidade_leitor_tela=compatibilidade_leitor_tela,
        )
        self._livros.append(novo_livro)
        return novo_livro
