from typing import List, Optional
import unicodedata

from data.livros import livros_iniciais
from models.livro import Livro


def _normalizar_busca(texto: str) -> str:
    """Ignora caixa e acentos, inclusive em textos Unicode decompostos."""
    return "".join(
        caractere
        for caractere in unicodedata.normalize("NFD", texto.casefold())
        if not unicodedata.combining(caractere)
    )


class LivroService:
    """Gerencia o catálogo de livros em memória."""

    RECURSOS_ACESSIBILIDADE = {
        "audiolivro",
        "braille",
        "ebook_acessivel",
        "fonte_ampliada",
        "compatibilidade_leitor_tela",
    }

    def __init__(self) -> None:
        self._livros: List[Livro] = livros_iniciais()

    def listar_livros(self) -> List[Livro]:
        """Retorna todos os livros cadastrados no catálogo."""
        return list(self._livros)

    def buscar_por_id(self, livro_id: int) -> Optional[Livro]:
        """Retorna o livro com o id informado, ou None se não existir."""
        return next((livro for livro in self._livros if livro.id == livro_id), None)

    def buscar_por_titulo_ou_autor(self, termo: str) -> List[Livro]:
        """Busca livros por trecho do título ou do autor, sem diferenciar caixa ou acentos."""
        termo_normalizado = _normalizar_busca(termo.strip())
        if not termo_normalizado:
            raise ValueError("O termo de busca não pode ficar vazio.")
        return [
            livro
            for livro in self._livros
            if termo_normalizado in _normalizar_busca(livro.titulo)
            or termo_normalizado in _normalizar_busca(livro.autor)
        ]

    def filtrar_por_acessibilidade(self, recursos: List[str]) -> List[Livro]:
        """Retorna obras que possuem todos os recursos informados (filtro AND)."""
        recursos_selecionados = set(recursos)
        desconhecidos = recursos_selecionados - self.RECURSOS_ACESSIBILIDADE
        if desconhecidos:
            raise ValueError(f"Recursos de acessibilidade inválidos: {', '.join(sorted(desconhecidos))}.")
        return [
            livro
            for livro in self._livros
            if all(getattr(livro, recurso) for recurso in recursos_selecionados)
        ]

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

    def atualizar_livro(
        self,
        livro_id: int,
        titulo: str,
        autor: str,
        ano_publicacao: int,
        audiolivro: Optional[bool] = None,
        braille: Optional[bool] = None,
        ebook_acessivel: Optional[bool] = None,
        fonte_ampliada: Optional[bool] = None,
        compatibilidade_leitor_tela: Optional[bool] = None,
    ) -> Optional[Livro]:
        """Atualiza um livro existente; retorna None quando o ID não existe."""
        indice = next(
            (indice for indice, livro in enumerate(self._livros) if livro.id == livro_id),
            None,
        )
        if indice is None:
            return None

        atual = self._livros[indice]
        atualizado = Livro(
            id=livro_id,
            titulo=titulo,
            autor=autor,
            ano_publicacao=ano_publicacao,
            audiolivro=atual.audiolivro if audiolivro is None else audiolivro,
            braille=atual.braille if braille is None else braille,
            ebook_acessivel=atual.ebook_acessivel if ebook_acessivel is None else ebook_acessivel,
            fonte_ampliada=atual.fonte_ampliada if fonte_ampliada is None else fonte_ampliada,
            compatibilidade_leitor_tela=(
                atual.compatibilidade_leitor_tela
                if compatibilidade_leitor_tela is None
                else compatibilidade_leitor_tela
            ),
        )
        self._livros[indice] = atualizado
        return atualizado

    def excluir_livro(self, livro_id: int) -> bool:
        """Remove um livro pelo ID e informa se ele foi encontrado."""
        livro = self.buscar_por_id(livro_id)
        if livro is None:
            return False
        self._livros.remove(livro)
        return True
