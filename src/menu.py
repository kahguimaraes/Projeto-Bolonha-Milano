from jogador import Jogador
from cidade import Cidade


class Menu:

    def __init__(self):
        self._em_execucao = True
        self._jogador = None
        self._cidade = None

    # Controla a execucao do menu
    def executar(self):
        while self._em_execucao:
            self.exibir_opcoes()
            opcao = self.ler_opcao()
            self.processar_opcao(opcao)

    # Mostra as opcoes do menu
    def exibir_opcoes(self):
        print("\n===== BOLONHA E MILANO =====")
        print("1 - Novo jogo")
        print("2 - Ver status da cidade")
        print("3 - Sobre o jogo")
        print("0 - Sair")

    # Le e valida a opcao digitada
    def ler_opcao(self):
        try:
            return int(input("Escolha uma opcao: "))
        except ValueError:
            return -1

    # Processa a opcao escolhida
    def processar_opcao(self, opcao):
        if opcao == 1:
            self.iniciar_novo_jogo()

        elif opcao == 2:
            self.exibir_status()

        elif opcao == 3:
            self.exibir_sobre()

        elif opcao == 0:
            print("Encerrando o jogo...")
            self._em_execucao = False

        else:
            print("Opcao invalida!")

    # Cria o jogador e a cidade
    def iniciar_novo_jogo(self):
        nome_jogador = input("Digite o nome do jogador: ").strip()
        nome_cidade = input("Digite o nome da cidade: ").strip()

        if not nome_jogador:
            nome_jogador = "Jogador 1"

        if not nome_cidade:
            nome_cidade = "Bolonha"

        self._jogador = Jogador(nome_jogador)
        self._cidade = Cidade(nome_cidade, self._jogador)

        print("\nNovo jogo iniciado!")
        self._cidade.exibir_status()

    # Verifica se existe um jogo iniciado
    def exibir_status(self):
        if self._cidade is None:
            print("Nenhum jogo iniciado!")
        else:
            self._cidade.exibir_status()

    # Mostra informacoes sobre o jogo
    def exibir_sobre(self):
        print("\nBolonha e Milano")
        print("Jogo de estrategia economica medieval.")
        print("Administre sua cidade e desenvolva seu territorio.")
