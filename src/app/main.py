from services.livro_service import LivroService


def exibir_menu() -> None:
    print("\n📚 LibraryFECAF")
    print("1. Listar livros")
    print("2. Cadastrar novo livro")
    print("3. Sair")


def ler_sim_nao(pergunta: str) -> bool:
    resposta = input(f"{pergunta} (s/n): ").strip().lower()
    return resposta in ("s", "sim")


def ler_ano(pergunta: str) -> int:
    while True:
        valor = input(pergunta).strip()
        try:
            return int(valor)
        except ValueError:
            print("Ano inválido. Digite apenas números, por exemplo: 1999.")


def listar_livros(service: LivroService) -> None:
    livros = service.listar_livros()
    if not livros:
        print("\nNenhum livro cadastrado.")
        return

    print(f"\nTotal de livros: {len(livros)}\n")
    for livro in livros:
        print(livro)
        print()


def cadastrar_livro(service: LivroService) -> None:
    print("\nCadastro de novo livro")
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
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
            print("Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
