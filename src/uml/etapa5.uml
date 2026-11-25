from jogador import Jogador
from cidade import Cidade
from mercado import Mercado
from agricultura import Agricultura
from governo import Governo


class Menu:

    def __init__(self):
        self._em_execucao = True
        self._jogador = None
        self._cidade = None
        self._mercado = Mercado()
        self._agricultura = Agricultura()
        self._governo = Governo()

    def executar(self):
        while self._em_execucao:
            self.exibir_opcoes()
            opcao = self.ler_opcao()
            self.processar_opcao(opcao)

    def exibir_opcoes(self):
        print("\n===== BOLONHA E MILANO =====")
        print("1 - Novo jogo")
        print("2 - Ver status da cidade")
        print("3 - Mercado")
        print("4 - Agricultura")
        print("5 - Governo")
        print("6 - Sobre o jogo")
        print("0 - Sair")

    def ler_opcao(self):
        try:
            return int(input("Escolha uma opcao: "))
        except ValueError:
            return -1

    def processar_opcao(self, opcao):
        if opcao == 1:
            self.iniciar_novo_jogo()

        elif opcao == 2:
            self.exibir_status()

        elif opcao == 3:
            self.abrir_mercado()

        elif opcao == 4:
            self.abrir_agricultura()

        elif opcao == 5:
            self.abrir_governo()

        elif opcao == 6:
            self.exibir_sobre()

        elif opcao == 0:
            print("Encerrando o jogo...")
            self._em_execucao = False

        else:
            print("Opcao invalida!")

    def iniciar_novo_jogo(self):
        nome_jogador = input("Nome do jogador: ").strip()
        nome_cidade = input("Nome da cidade: ").strip()

        if not nome_jogador:
            nome_jogador = "Jogador 1"

        if not nome_cidade:
            nome_cidade = "Bolonha"

        self._jogador = Jogador(nome_jogador)
        self._cidade = Cidade(nome_cidade, self._jogador)

        print("\nNovo jogo iniciado!")
        self._cidade.exibir_status()

    def exibir_status(self):
        if self._cidade is None:
            print("Nenhum jogo iniciado!")
        else:
            self._cidade.exibir_status()

    # MERCADO
    def abrir_mercado(self):
        if self._cidade is None:
            print("Inicie um jogo primeiro!")
            return

        while True:
            print("\n===== MERCADO =====")
            print(f"Florins disponiveis: {self._cidade.get_florins()}")
            print(f"Preco do grao: {self._mercado.get_preco_grao()}")
            print(f"Preco da terra: {self._mercado.get_preco_terra()}")

            print("1 - Comprar graos")
            print("2 - Vender graos")
            print("3 - Comprar terras")
            print("4 - Vender terras")
            print("0 - Voltar")

            opcao = self.ler_opcao()

            if opcao == 1:
                self.comprar_graos()

            elif opcao == 2:
                self.vender_graos()

            elif opcao == 3:
                self.comprar_terras()

            elif opcao == 4:
                self.vender_terras()

            elif opcao == 0:
                break

            else:
                print("Opcao invalida!")

    def ler_quantidade(self):
        try:
            qtd = int(input("Digite a quantidade: "))

            if qtd > 0:
                return qtd

        except ValueError:
            pass

        return 0

    def comprar_graos(self):
        qtd = self.ler_quantidade()

        if self._mercado.comprar_graos(self._cidade, qtd):
            print("Compra realizada com sucesso!")
        else:
            print("Quantidade invalida ou saldo insuficiente!")

    def vender_graos(self):
        qtd = self.ler_quantidade()

        if self._mercado.vender_graos(self._cidade, qtd):
            print("Venda realizada com sucesso!")
        else:
            print("Quantidade invalida ou graos insuficientes!")

    def comprar_terras(self):
        qtd = self.ler_quantidade()

        if self._mercado.comprar_terras(self._cidade, qtd):
            print("Compra realizada com sucesso!")
        else:
            print("Quantidade invalida ou saldo insuficiente!")

    def vender_terras(self):
        qtd = self.ler_quantidade()

        if self._mercado.vender_terras(self._cidade, qtd):
            print("Venda realizada com sucesso!")
        else:
            print("Quantidade invalida ou terras insuficientes!")

    # AGRICULTURA
    def abrir_agricultura(self):
        if self._cidade is None:
            print("Inicie um jogo primeiro!")
            return

        while True:
            print("\n===== AGRICULTURA =====")
            print(f"Terras: {self._cidade.get_terras()}")
            print(f"Servos: {self._cidade.get_servos()}")
            print(f"Graos: {self._cidade.get_graos()}")

            print("1 - Colher")
            print("2 - Distribuir alimentos")
            print("0 - Voltar")

            opcao = self.ler_opcao()

            if opcao == 1:
                self.colher()

            elif opcao == 2:
                self.distribuir_alimentos()

            elif opcao == 0:
                break

            else:
                print("Opcao invalida!")

    def colher(self):
        self._agricultura.processar_colheita(self._cidade)

    def distribuir_alimentos(self):
        print("Informe um percentual entre 20 e 80.")

        try:
            percentual = int(input("Percentual: "))
        except ValueError:
            print("Percentual invalido!")
            return

        resultado = self._agricultura.distribuir_alimentos(
            self._cidade, percentual
        )

        if resultado:
            print("Alimentos distribuidos com sucesso!")
        else:
            print("Percentual invalido!")

    # GOVERNO
    def abrir_governo(self):
        if self._cidade is None:
            print("Inicie um jogo primeiro!")
            return

        while True:
            print("\n===== GOVERNO =====")
            print(f"Florins: {self._cidade.get_florins()}")
            print(f"Taxa de imposto: {self._cidade.get_taxa_imposto()}%")
            print(f"Nivel de justica: {self._cidade.get_nivel_justica()}")

            print("1 - Arrecadar impostos")
            print("2 - Definir taxa de imposto")
            print("3 - Definir nivel de justica")
            print("0 - Voltar")

            opcao = self.ler_opcao()

            if opcao == 1:
                self.arrecadar_impostos()

            elif opcao == 2:
                self.definir_taxa_imposto()

            elif opcao == 3:
                self.definir_justica()

            elif opcao == 0:
                break

            else:
                print("Opcao invalida!")

    def arrecadar_impostos(self):
        arrecadado = self._governo.arrecadar_impostos(
            self._cidade
        )

        print("\n===== ARRECADACAO DE IMPOSTOS =====")
        print(f"Florins arrecadados: {arrecadado}")
        print(f"Saldo atual: {self._cidade.get_florins()}")

    def definir_taxa_imposto(self):
        print("Informe uma taxa entre 0 e 50.")

        try:
            taxa = int(input("Nova taxa de imposto: "))
        except ValueError:
            print("Taxa invalida!")
            return

        if self._governo.definir_taxa_imposto(self._cidade, taxa):
            print("Taxa de imposto atualizada!")
        else:
            print("Taxa invalida!")

    def definir_justica(self):
        print("\n===== NIVEIS DE JUSTICA =====")
        print("1 - Justa")
        print("2 - Moderada")
        print("3 - Severa")

        opcao = self.ler_opcao()

        niveis = {
            1: "Justa",
            2: "Moderada",
            3: "Severa"
        }

        nivel = niveis.get(opcao, "")

        if self._governo.definir_justica(self._cidade, nivel):
            print("Nivel de justica atualizado!")
        else:
            print("Nivel de justica invalido!")

    def exibir_sobre(self):
        print("\nBolonha e Milano")
        print("Jogo de estrategia economica medieval.")
        print("Administre sua cidade e desenvolva seu territorio.")
