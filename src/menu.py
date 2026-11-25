from jogador import Jogador
from cidade import Cidade
from mercado import Mercado
from agricultura import Agricultura
from governo import Governo
from construcoes import Construcoes
from nobreza import Nobreza
from partida import Partida


class Menu:

    def __init__(self):
        self._em_execucao = True
        self._partida = None
        self._cidade = None
        self._mercado = Mercado()
        self._agricultura = Agricultura()
        self._governo = Governo()
        self._construcoes = Construcoes()
        self._nobreza = Nobreza()

    def executar(self):
        while self._em_execucao:
            self.exibir_opcoes()
            opcao = self.ler_opcao()
            self.processar_opcao(opcao)

    def exibir_opcoes(self):
        print("\n===== BOLONHA E MILANO =====")

        if self._cidade is not None:
            print(f"Ano: {self._cidade.get_ano_atual()}")
            print(f"Cidade: {self._cidade.get_nome()}")
            print(f"Vez de: {self._cidade.get_dono().get_nome()}")

        print("1 - Novo jogo")
        print("2 - Ver status da cidade")
        print("3 - Mercado")
        print("4 - Agricultura")
        print("5 - Governo")
        print("6 - Construcoes")
        print("7 - Encerrar turno")
        print("8 - Ver classificacao")
        print("9 - Sobre o jogo")
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
            self.abrir_construcoes()

        elif opcao == 7:
            self.encerrar_turno()

        elif opcao == 8:
            self.exibir_classificacao()

        elif opcao == 9:
            self.exibir_sobre()

        elif opcao == 0:
            print("Encerrando o jogo...")
            self._em_execucao = False

        else:
            print("Opcao invalida!")

    # NOVA PARTIDA
    def iniciar_novo_jogo(self):
        print("\n===== NOVO JOGO =====")
        print("Quantos jogadores? (1 a 4)")

        quantidade = self.ler_opcao()

        if not 1 <= quantidade <= 4:
            quantidade = 2
            print("Quantidade invalida. Serao 2 jogadores.")

        self._partida = Partida()

        cidades = ["Bolonha", "Milano", "Florenca", "Veneza"]

        for i in range(quantidade):
            print(f"\nJogador {i + 1}")

            nome = input("Nome do jogador: ").strip()

            if not nome:
                nome = f"Jogador {i + 1}"

            jogador = Jogador(nome)
            cidade = Cidade(cidades[i], jogador)

            self._partida.adicionar_cidade(cidade)

            print(f"Cidade: {cidade.get_nome()}")

        self._cidade = self._partida.get_cidade_atual()

        print("\nPartida iniciada!")
        self._cidade.exibir_status()

    def exibir_status(self):
        if self._cidade is None:
            print("Nenhum jogo iniciado!")
            return

        self._cidade.exibir_status()

        prestigio = self._nobreza.calcular_prestigio(
            self._cidade
        )

        print(f"Prestigio: {prestigio}")

    # MERCADO
    def abrir_mercado(self):
        if self._cidade is None:
            print("Inicie um jogo primeiro!")
            return

        while True:
            print("\n===== MERCADO =====")
            print(f"Florins: {self._cidade.get_florins()}")
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
        resultado = self._agricultura.processar_colheita(
            self._cidade
        )

        if resultado == -1:
            print("A colheita deste ano ja foi realizada!")

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

        if arrecadado == -1:
            print("Os impostos deste ano ja foram arrecadados!")
            return

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

    # CONSTRUCOES
    def abrir_construcoes(self):
        if self._cidade is None:
            print("Inicie um jogo primeiro!")
            return

        while True:
            print("\n===== CONSTRUCOES =====")
            print(f"Florins: {self._cidade.get_florins()}")
            print(f"Servos: {self._cidade.get_servos()}")
            print(f"Soldados: {self._cidade.get_soldados()}")
            print(f"Construcoes: {self._cidade.get_construcoes()}")

            print("1 - Recrutar soldados")
            print("2 - Construir")
            print("0 - Voltar")

            opcao = self.ler_opcao()

            if opcao == 1:
                self.recrutar_soldados()

            elif opcao == 2:
                self.construir()

            elif opcao == 0:
                break

            else:
                print("Opcao invalida!")

    def recrutar_soldados(self):
        print("Custo por soldado: 5 florins e 1 servo.")

        qtd = self.ler_quantidade()

        if self._construcoes.recrutar_soldados(self._cidade, qtd):
            print("Recrutamento realizado com sucesso!")
        else:
            print("Quantidade invalida ou recursos insuficientes!")

    def construir(self):
        print("Custo por construcao: 20 florins.")

        qtd = self.ler_quantidade()

        if self._construcoes.construir(self._cidade, qtd):
            print("Construcao realizada com sucesso!")
        else:
            print("Quantidade invalida ou saldo insuficiente!")

    # CONTROLE DOS TURNOS
    def encerrar_turno(self):
        if self._partida is None:
            print("Inicie um jogo primeiro!")
            return

        ano_encerrado = self._partida.passar_turno()

        if ano_encerrado:
            print("\n===== FIM DO ANO =====")

            promovidas = self._partida.encerrar_ano(
                self._nobreza
            )

            for cidade in promovidas:
                jogador = cidade.get_dono()

                print(
                    f"{jogador.get_nome()} foi promovido "
                    f"para {jogador.get_titulo()}!"
                )

            self.exibir_classificacao()

            if self._partida.terminou():
                self.encerrar_partida()
                return

            print(f"\nNovo ano: {self._partida.get_ano_atual()}")

        self._cidade = self._partida.get_cidade_atual()

        print(f"\nAgora e a vez de {self._cidade.get_dono().get_nome()}!")
        print(f"Cidade: {self._cidade.get_nome()}")

    # CLASSIFICACAO
    def exibir_classificacao(self):
        if self._partida is None:
            print("Nenhuma partida iniciada!")
            return

        cidades = sorted(
            self._partida.get_cidades(),
            key=lambda cidade: (
                cidade.get_dono().get_nivel_titulo(),
                self._nobreza.calcular_prestigio(cidade)
            ),
            reverse=True
        )

        print("\n===== CLASSIFICACAO =====")

        for posicao, cidade in enumerate(cidades, start=1):
            jogador = cidade.get_dono()

            prestigio = self._nobreza.calcular_prestigio(
                cidade
            )

            necessario = self._nobreza.prestigio_para_proximo_titulo(
                jogador
            )

            print(f"\n{posicao} - {cidade.get_nome()}")
            print(f"Governante: {jogador.get_nome()}")
            print(f"Titulo: {jogador.get_titulo()}")
            print(f"Prestigio: {prestigio}")

            if necessario == -1:
                print("Titulo maximo atingido!")
            else:
                faltam = max(0, necessario - prestigio)
                print(f"Faltam {faltam} pontos para o proximo titulo.")

    # ENCERRAMENTO DA PARTIDA
    def encerrar_partida(self):
        vencedor = self._partida.determinar_vencedor(
            self._nobreza
        )

        print("\n===== FIM DA PARTIDA =====")

        if vencedor is not None:
            jogador = vencedor.get_dono()

            print(f"Vencedor: {jogador.get_nome()}")
            print(f"Cidade: {vencedor.get_nome()}")
            print(f"Titulo: {jogador.get_titulo()}")
            print(f"Prestigio: {self._nobreza.calcular_prestigio(vencedor)}")

        self._partida = None
        self._cidade = None

        print("Obrigado por jogar!")

    def exibir_sobre(self):
        print("\nBolonha e Milano")
        print("Jogo de estrategia economica medieval.")
        print("De 1 a 4 jogadores.")
        print("Administre sua cidade e conquiste prestigio.")
        print("Alcance o titulo de Rei/Rainha ou lidere em 1410.")
