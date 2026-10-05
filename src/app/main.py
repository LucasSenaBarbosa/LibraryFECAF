from typing import List, Optional

from services.livro_service import LivroService

RECURSOS_ACESSIBILIDADE = {
    "1": ("audiolivro", "Audiolivro"),
    "2": ("braille", "Braille"),
    "3": ("ebook_acessivel", "E-book acessível"),
    "4": ("fonte_ampliada", "Fonte ampliada"),
    "5": ("compatibilidade_leitor_tela", "Compatibilidade com leitor de tela"),
}


def exibir_menu() -> None:
    print("\n📚 LibraryFECAF")
    print("1. Listar livros")
    print("2. Cadastrar novo livro")
    print("3. Buscar por título ou autor")
    print("4. Buscar por acessibilidade")
    print("5. Editar livro")
    print("6. Excluir livro")
    print("7. Resumo do catálogo")
    print("8. Sair")


def ler_texto(pergunta: str, valor_atual: str = "") -> str:
    while True:
        sufixo = f" [{valor_atual}] (Enter mantém)" if valor_atual else ""
        valor = input(f"{pergunta}{sufixo}: ").strip()
        if valor:
            return valor
        if valor_atual:
            return valor_atual
        print("Este campo é obrigatório.")


def ler_sim_nao(pergunta: str, valor_atual: Optional[bool] = None) -> bool:
    while True:
        sufixo = " [s/n, Enter mantém]" if valor_atual is not None else " (s/n)"
        resposta = input(f"{pergunta}{sufixo}: ").strip().lower()
        if not resposta and valor_atual is not None:
            return valor_atual
        if resposta in ("s", "sim"):
            return True
        if resposta in ("n", "nao", "não"):
            return False
        print("Resposta inválida. Digite s ou n.")


def ler_ano(pergunta: str, valor_atual: Optional[int] = None) -> int:
    while True:
        sufixo = f" [{valor_atual}] (Enter mantém): " if valor_atual is not None else ": "
        valor = input(f"{pergunta}{sufixo}").strip()
        if not valor and valor_atual is not None:
            return valor_atual
        try:
            ano = int(valor)
            if ano > 0:
                return ano
        except ValueError:
            pass
        print("Ano inválido. Digite um número inteiro positivo, por exemplo: 1999.")


def ler_id() -> int:
    while True:
        try:
            livro_id = int(input("ID do livro: ").strip())
            if livro_id > 0:
                return livro_id
        except ValueError:
            pass
        print("ID inválido. Digite um número inteiro positivo.")


def exibir_resultados(livros: List) -> None:
    if not livros:
        print("\nNenhum livro encontrado para os critérios informados.")
        return
    print(f"\nLivros encontrados: {len(livros)}\n")
    for livro in livros:
        print(livro)
        print()


def listar_livros(service: LivroService) -> None:
    livros = service.listar_livros()
    print(f"\nTotal de livros: {len(livros)}")
    exibir_resultados(livros)


def exibir_resumo_catalogo(service: LivroService) -> None:
    resumo = service.obter_resumo_catalogo()
    nomes = {
        "audiolivro": "Audiolivro",
        "braille": "Braille",
        "ebook_acessivel": "E-book acessível",
        "fonte_ampliada": "Fonte ampliada",
        "compatibilidade_leitor_tela": "Compatibilidade com leitor de tela",
    }

    print(f"\n📊 Resumo do catálogo")
    print(f"Total de livros: {resumo['total_livros']}")
    print("\nRecursos de acessibilidade:")
    for recurso, nome in nomes.items():
        print(f"- {nome}: {resumo[recurso]} livro(s)")


def cadastrar_livro(service: LivroService) -> None:
    print("\nCadastro de novo livro")
    titulo = ler_texto("Título")
    autor = ler_texto("Autor")
    ano_publicacao = ler_ano("Ano de publicação: ")

    print("\nRecursos de acessibilidade disponíveis nesta obra:")
    audiolivro = ler_sim_nao("Possui audiolivro?")
    braille = ler_sim_nao("Possui versão em braille?")
    ebook_acessivel = ler_sim_nao("Possui e-book acessível?")
    fonte_ampliada = ler_sim_nao("Possui fonte ampliada?")
    compatibilidade_leitor_tela = ler_sim_nao("É compatível com leitor de tela?")

    livro = service.cadastrar_livro(
        titulo=titulo,
        autor=autor,
        ano_publicacao=ano_publicacao,
        audiolivro=audiolivro,
        braille=braille,
        ebook_acessivel=ebook_acessivel,
        fonte_ampliada=fonte_ampliada,
        compatibilidade_leitor_tela=compatibilidade_leitor_tela,
    )

    print(f"\nLivro cadastrado com sucesso!\n{livro}")


def buscar_livros(service: LivroService) -> None:
    termo = ler_texto("Digite o título ou autor")
    exibir_resultados(service.buscar_por_titulo_ou_autor(termo))


def buscar_por_acessibilidade(service: LivroService) -> None:
    print("\nSelecione um ou mais recursos:")
    for numero, (_, nome) in RECURSOS_ACESSIBILIDADE.items():
        print(f"{numero}. {nome}")

    while True:
        selecao = input("Recursos (separados por vírgula, ex.: 1, 3): ").strip()
        numeros = [item.strip() for item in selecao.split(",")]
        if numeros and all(numero in RECURSOS_ACESSIBILIDADE for numero in numeros):
            recursos = [RECURSOS_ACESSIBILIDADE[numero][0] for numero in set(numeros)]
            exibir_resultados(service.filtrar_por_acessibilidade(recursos))
            return
        print("Seleção inválida. Informe os números de 1 a 5, separados por vírgula.")


def editar_livro(service: LivroService) -> None:
    livro = service.buscar_por_id(ler_id())
    if livro is None:
        print("Livro não encontrado.")
        return

    print(f"\nEditando livro: {livro}")
    atualizado = service.atualizar_livro(
        livro_id=livro.id,
        titulo=ler_texto("Título", livro.titulo),
        autor=ler_texto("Autor", livro.autor),
        ano_publicacao=ler_ano("Ano de publicação", livro.ano_publicacao),
        audiolivro=ler_sim_nao("Possui audiolivro?", livro.audiolivro),
        braille=ler_sim_nao("Possui versão em braille?", livro.braille),
        ebook_acessivel=ler_sim_nao("Possui e-book acessível?", livro.ebook_acessivel),
        fonte_ampliada=ler_sim_nao("Possui fonte ampliada?", livro.fonte_ampliada),
        compatibilidade_leitor_tela=ler_sim_nao(
            "É compatível com leitor de tela?", livro.compatibilidade_leitor_tela
        ),
    )
    print(f"\nLivro atualizado com sucesso!\n{atualizado}")


def excluir_livro(service: LivroService) -> None:
    livro_id = ler_id()
    livro = service.buscar_por_id(livro_id)
    if livro is None:
        print("Livro não encontrado.")
        return
    print(livro)
    if ler_sim_nao("Confirma a exclusão?"):
        service.excluir_livro(livro_id)
        print("Livro excluído com sucesso.")
    else:
        print("Exclusão cancelada.")


def main() -> None:
    service = LivroService()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            listar_livros(service)
        elif opcao == "2":
            cadastrar_livro(service)
        elif opcao == "3":
            buscar_livros(service)
        elif opcao == "4":
            buscar_por_acessibilidade(service)
        elif opcao == "5":
            editar_livro(service)
        elif opcao == "6":
            excluir_livro(service)
        elif opcao == "7":
            exibir_resumo_catalogo(service)
        elif opcao == "8":
            print("Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
