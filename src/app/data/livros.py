from typing import List

from models.livro import Livro


def livros_iniciais() -> List[Livro]:
    """Retorna a lista inicial de 10 livros cadastrados no catálogo."""

    return [
        Livro(
            id=1,
            titulo="Dom Casmurro",
            autor="Machado de Assis",
            ano_publicacao=1899,
            audiolivro=True,
            ebook_acessivel=True,
            compatibilidade_leitor_tela=True,
        ),
        Livro(
            id=2,
            titulo="O Pequeno Príncipe",
            autor="Antoine de Saint-Exupéry",
            ano_publicacao=1943,
            audiolivro=True,
            braille=True,
            fonte_ampliada=True,
        ),
        Livro(
            id=3,
            titulo="Grande Sertão: Veredas",
            autor="João Guimarães Rosa",
            ano_publicacao=1956,
            ebook_acessivel=True,
            compatibilidade_leitor_tela=True,
        ),
        Livro(
            id=4,
            titulo="A Hora da Estrela",
            autor="Clarice Lispector",
            ano_publicacao=1977,
            audiolivro=True,
            fonte_ampliada=True,
        ),
        Livro(
            id=5,
            titulo="1984",
            autor="George Orwell",
            ano_publicacao=1949,
            audiolivro=True,
            braille=True,
            ebook_acessivel=True,
            compatibilidade_leitor_tela=True,
        ),
        Livro(
            id=6,
            titulo="Vidas Secas",
            autor="Graciliano Ramos",
            ano_publicacao=1938,
            fonte_ampliada=True,
        ),
        Livro(
            id=7,
            titulo="O Cortiço",
            autor="Aluísio Azevedo",
            ano_publicacao=1890,
            ebook_acessivel=True,
        ),
        Livro(
            id=8,
            titulo="Memórias Póstumas de Brás Cubas",
            autor="Machado de Assis",
            ano_publicacao=1881,
            audiolivro=True,
            braille=True,
            ebook_acessivel=True,
            fonte_ampliada=True,
            compatibilidade_leitor_tela=True,
        ),
        Livro(
            id=9,
            titulo="Capitães da Areia",
            autor="Jorge Amado",
            ano_publicacao=1937,
            audiolivro=True,
        ),
        Livro(
            id=10,
            titulo="Iracema",
            autor="José de Alencar",
            ano_publicacao=1865,
            braille=True,
            compatibilidade_leitor_tela=True,
        ),
    ]
