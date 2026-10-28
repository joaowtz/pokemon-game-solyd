# Jogo Pokémon de Terminal

Um jogo simples de Pokémon desenvolvido em Python para ser executado no
terminal. O jogador pode escolher um Pokémon inicial, explorar, capturar
Pokémon, batalhar contra inimigos e ganhar dinheiro.

Este projeto foi desenvolvido como estudo durante o curso **Python Orientado a
Objetos e Automação**, da [Solyd](https://solyd.com.br/). A prática envolve
conceitos de Python, programação orientada a objetos, herança, interação com o
usuário e criação de projetos.

## Funcionalidades

- Escolha entre Pikachu, Charmander e Squirtle como Pokémon inicial.
- Exploração com possibilidade de encontrar e capturar Pokémon selvagens.
- Batalhas contra inimigos com Pokémon aleatórios.
- Exibição dos Pokémon e do dinheiro do jogador.
- Salvamento e carregamento do progresso em um arquivo local.

## Arquivos do projeto

- `main.py`: inicia o jogo e apresenta o menu principal.
- `Pokemon.py`: contém as classes dos Pokémon e seus ataques.
- `Pessoas.py`: contém as classes do jogador, inimigos e regras de batalha.
- `database.db`: arquivo criado automaticamente para salvar o jogo.

## Requisitos

- Python 3 instalado.
- Não é necessário instalar bibliotecas externas; o projeto usa apenas módulos
  da biblioteca padrão do Python.

## Como executar

Abra o terminal na pasta do projeto e execute:

```bash
python main.py
```

Em alguns sistemas, pode ser necessário usar:

```bash
python3 main.py
```

## Como jogar

Depois de iniciar o jogo:

1. Informe um nickname.
2. Escolha um Pokémon inicial.
3. Use o menu para explorar, batalhar ou consultar suas informações.
4. Escolha a opção `5` para salvar o progresso e sair.

O progresso é salvo no arquivo `database.db` e carregado automaticamente na
próxima execução.

## Observação

Este projeto foi criado para fins de estudo de Python, programação orientada a
objetos, herança, interação com o usuário e persistência de dados com
`pickle`.
