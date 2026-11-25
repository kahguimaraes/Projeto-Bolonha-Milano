# Bolonha e Milano

## Sobre o projeto

Bolonha e Milano é um jogo de estratégia e administração
econômica medieval desenvolvido em Python.

O objetivo é administrar uma cidade, controlar seus recursos,
desenvolver a economia e conquistar prestígio para alcançar
o título de Rei/Rainha.

O jogo permite partidas de 1 a 4 jogadores, entre os anos
de 1400 e 1410.

## Tecnologias utilizadas

- Python 3
- Visual Studio Code
- Git
- GitHub
- PlantUML

## Funcionalidades

- Cadastro de jogadores e cidades
- Controle dos recursos da cidade
- Compra e venda de grãos e terras
- Agricultura e distribuição de alimentos
- Arrecadação de impostos
- Administração do governo
- Construções e soldados
- Sistema de turnos anuais
- Sistema de prestígio e títulos
- Classificação e determinação do vencedor
- Testes automatizados

## Como executar

É necessário possuir o Python 3 instalado.

Abra o terminal na raiz do projeto e execute:

    python src/main.py

No Windows, também é possível utilizar:

    py src/main.py

Não é necessário instalar bibliotecas externas.

## Como jogar

1. Novo jogo
2. Ver status da cidade
3. Mercado
4. Agricultura
5. Governo
6. Construções
7. Encerrar turno
8. Ver classificação
9. Sobre o jogo
0. Sair

Cada jogador administra sua cidade durante seu turno.
Quando todos encerram seus turnos, o ano avança.

## Condições de vitória

O vencedor será o jogador que alcançar o título de
Rei/Rainha ou possuir a melhor classificação ao final
do ano de 1410.

A classificação considera o título e o prestígio.

## Como executar os testes

Execute no terminal:

    python src/testes.py

Ou, no Windows:

    py src/testes.py

Resultado esperado:

    Aprovados: 37 | Reprovados: 0

## Organização do projeto

    src/
        main.py
        menu.py
        jogador.py
        cidade.py
        mercado.py
        agricultura.py
        governo.py
        construcoes.py
        nobreza.py
        partida.py
        testes.py

    uml/
    casos-de-uso/
    README.md
    .gitignore

## Etapas do desenvolvimento

- Etapa 1: Estrutura inicial e menu
- Etapa 2: Jogador e cidade
- Etapa 3: Economia e mercado
- Etapa 4: Agricultura e população
- Etapa 5: Impostos e governo
- Etapa 6: Construções e soldados
- Etapa 7: Rodadas, jogadores e vitória
- Etapa 8: Integração, testes e entrega final

## Informações acadêmicas

Disciplina: Desenvolvimento de Sistemas

Professor: Domingos Bernardo

Projeto do quarto bimestre de 2026.
