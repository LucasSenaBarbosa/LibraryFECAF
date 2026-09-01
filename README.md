# 📚 LibraryFECAF

Projeto desenvolvido em Python com o objetivo de criar um catálogo de livros
que possuam diferentes recursos de acessibilidade.

A proposta é facilitar a descoberta de livros por pessoas com deficiência,
permitindo que elas encontrem obras de acordo com os formatos e recursos
acessíveis disponíveis.

## 🎯 Objetivo

Criar um espaço onde pessoas com diferentes necessidades possam encontrar
livros que sejam compatíveis com suas formas de leitura e consumo de
conteúdo.

O projeto inicialmente terá uma lista de livros cadastrados e permitirá o
cadastro de novas obras juntamente com suas características de
acessibilidade.

## 🚀 Funcionalidades iniciais

Na primeira versão, a aplicação:

- Exibe uma lista inicial de 10 livros;
- Exibe as informações básicas de cada livro;
- Informa quais recursos de acessibilidade estão disponíveis para cada obra;
- Permite o cadastro de novos livros;
- Permite informar os recursos de acessibilidade disponíveis em cada livro.

## 📖 Informações dos livros

Cada livro possui inicialmente:

- ID
- Título
- Autor
- Ano de publicação
- Audiolivro
- Braille
- E-book acessível
- Fonte ampliada
- Compatibilidade com leitor de tela

Essas características poderão ser ampliadas conforme os requisitos do
projeto.

## ♿ Acessibilidade dos livros

A acessibilidade é o principal foco do projeto.

O sistema permite identificar quais recursos estão disponíveis em cada
livro. Dessa forma, uma pessoa poderá futuramente buscar obras que atendam
às suas necessidades específicas.

Por exemplo, uma pessoa que utiliza audiolivros poderá procurar somente
livros que possuam uma versão em audiolivro. Outra pessoa que utiliza leitor
de tela poderá procurar livros disponíveis em formatos compatíveis com essa
tecnologia.

A proposta não é considerar um livro simplesmente como "acessível" ou "não
acessível", mas informar quais recursos de acessibilidade ele possui. Veja
mais detalhes em [docs/acessibilidade.md](docs/acessibilidade.md).

## 🛠️ Tecnologias

- Python
- Git
- GitHub

Outras tecnologias poderão ser adicionadas conforme o projeto evoluir.

## ▶️ Como executar

```bash
# Instalar dependências (necessário apenas para rodar os testes)
pip install -r requirements.txt

# Executar a aplicação
python src/app/main.py

# Executar os testes
pytest
```

## 📁 Estrutura do projeto

```
LibraryFECAF/
│
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
│
├── src/
│   └── app/
│       ├── main.py
│       │
│       ├── models/
│       │   └── livro.py
│       │
│       ├── services/
│       │   └── livro_service.py
│       │
│       └── data/
│           └── livros.py
│
├── tests/
│   └── test_livros.py
│
├── docs/
│   └── acessibilidade.md
│
└── .github/
    └── workflows/
        └── tests.yml
```

## 👥 Equipe

O projeto será desenvolvido de forma colaborativa.

As responsabilidades poderão ser divididas entre:

- Desenvolvimento;
- Testes;
- Documentação;
- Pesquisa sobre acessibilidade;
- Cadastro e organização dos livros;
- Análise de requisitos.

## 🌱 Status do projeto

Em desenvolvimento — MVP

### Próximos passos

- [x] Definir os recursos de acessibilidade que serão utilizados;
- [x] Criar os 10 livros iniciais;
- [x] Criar o modelo Livro;
- [x] Implementar a listagem dos livros;
- [x] Implementar o cadastro de novos livros;
- [x] Implementar testes;
- [ ] Planejar a busca por recursos de acessibilidade.

## 🔮 Futuras funcionalidades

Após o MVP, o projeto poderá evoluir para incluir:

- Busca por título e autor;
- Filtros por recursos de acessibilidade;
- Cadastro de diferentes formatos do mesmo livro;
- Perfis de usuários;
- Recomendações de livros;
- Avaliações sobre a acessibilidade das obras;
- Informações sobre onde encontrar cada formato acessível.

## 🤝 Contribuição

O projeto será desenvolvido de forma colaborativa utilizando Git e GitHub.

Cada integrante deverá trabalhar preferencialmente em uma branch própria. As
alterações serão integradas ao projeto principal por meio de Pull Requests e
revisão da equipe.

## 📄 Licença

Este projeto está disponibilizado sob a licença [MIT](LICENSE).
