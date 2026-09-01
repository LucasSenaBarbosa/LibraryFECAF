from dataclasses import dataclass
from typing import List


@dataclass
class Livro:
    """Representa um livro do catálogo e seus recursos de acessibilidade."""

    id: int
    titulo: str
    autor: str
    ano_publicacao: int
    audiolivro: bool = False
    braille: bool = False
    ebook_acessivel: bool = False
    fonte_ampliada: bool = False
    compatibilidade_leitor_tela: bool = False

    def __post_init__(self) -> None:
        if self.ano_publicacao <= 0:
            raise ValueError("ano_publicacao deve ser um número positivo.")

    def recursos_disponiveis(self) -> List[str]:
        """Lista os nomes dos recursos de acessibilidade marcados como disponíveis."""
        recursos = {
            "Audiolivro": self.audiolivro,
            "Braille": self.braille,
            "E-book acessível": self.ebook_acessivel,
            "Fonte ampliada": self.fonte_ampliada,
            "Compatível com leitor de tela": self.compatibilidade_leitor_tela,
        }
        return [nome for nome, disponivel in recursos.items() if disponivel]

    def __str__(self) -> str:
        recursos = self.recursos_disponiveis()
        recursos_str = ", ".join(recursos) if recursos else "Nenhum recurso de acessibilidade cadastrado"
        return (
            f"[{self.id}] {self.titulo} - {self.autor} ({self.ano_publicacao})\n"
            f"    Recursos de acessibilidade: {recursos_str}"
        )
