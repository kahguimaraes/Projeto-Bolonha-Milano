from cidade import Cidade
from jogador import Jogador
from mercado import Mercado
from agricultura import Agricultura
from governo import Governo
from construcoes import Construcoes
from nobreza import Nobreza
from partida import Partida


class Testes:

    aprovados = 0
    reprovados = 0

    @staticmethod
    def verificar(descricao, condicao):
        if condicao:
            Testes.aprovados += 1
            print(f"[OK] {descricao}")
        else:
            Testes.reprovados += 1
            print(f"[FALHA] {descricao}")

    @staticmethod
    def nova_cidade():
        return Cidade("Bolonha", Jogador("Teste"))

    # TESTES DA CIDADE
    @staticmethod
    def testar_cidade():
        print("\n--- CIDADE ---")

        cidade = Testes.nova_cidade()

        Testes.verificar(
            "Cidade nasce com 1000 florins",
            cidade.get_florins() == 1000
        )

        Testes.verificar(
            "Cidade nasce no ano 1400",
            cidade.get_ano_atual() == 1400
        )

        resultado = cidade.remover_florins(2000)

        Testes.verificar(
            "Remover florins acima do saldo e recusado",
            not resultado
        )

        Testes.verificar(
            "Saldo permanece igual",
            cidade.get_florins() == 1000
        )

        cidade.marcar_colheita_feita()
        cidade.avancar_ano()

        Testes.verificar(
            "Avancar ano soma 1",
            cidade.get_ano_atual() == 1401
        )

        Testes.verificar(
            "Novo ano libera a colheita",
            not cidade.is_colheita_feita()
        )

    # TESTES DO MERCADO
    @staticmethod
    def testar_mercado():
        print("\n--- MERCADO ---")

        cidade = Testes.nova_cidade()
        mercado = Mercado()

        resultado = mercado.comprar_graos(cidade, 100)

        Testes.verificar(
            "Comprar 100 graos funciona",
            resultado
        )

        Testes.verificar(
            "Compra custa 200 florins",
            cidade.get_florins() == 800
        )

        Testes.verificar(
            "Compra adiciona 100 graos",
            cidade.get_graos() == 600
        )

        Testes.verificar(
            "Quantidade negativa e recusada",
            not mercado.comprar_graos(cidade, -10)
        )

        Testes.verificar(
            "Compra sem saldo e recusada",
            not mercado.comprar_graos(cidade, 10000)
        )

    # TESTES DA AGRICULTURA
    @staticmethod
    def testar_agricultura():
        print("\n--- AGRICULTURA ---")

        cidade = Testes.nova_cidade()
        agricultura = Agricultura()

        resultado = agricultura.processar_colheita(cidade)

        Testes.verificar(
            "Primeira colheita cultiva 1000 hectares",
            resultado == 1000
        )

        Testes.verificar(
            "Estoque final de 2000 graos",
            cidade.get_graos() == 2000
        )

        Testes.verificar(
            "Segunda colheita no ano e recusada",
            agricultura.processar_colheita(cidade) == -1
        )

        Testes.verificar(
            "Distribuir 10 por cento e recusado",
            not agricultura.distribuir_alimentos(cidade, 10)
        )

    # TESTES DO GOVERNO
    @staticmethod
    def testar_governo():
        print("\n--- GOVERNO ---")

        cidade = Testes.nova_cidade()
        governo = Governo()

        Testes.verificar(
            "Taxa de 60 por cento e recusada",
            not governo.definir_taxa_imposto(cidade, 60)
        )

        Testes.verificar(
            "Justica invalida e recusada",
            not governo.definir_justica(cidade, "Branda")
        )

        governo.definir_taxa_imposto(cidade, 10)
        governo.definir_justica(cidade, "Severa")

        resultado = governo.arrecadar_impostos(cidade)

        Testes.verificar(
            "Arrecadacao de 26 florins",
            resultado == 26
        )

        Testes.verificar(
            "Segunda arrecadacao no ano e recusada",
            governo.arrecadar_impostos(cidade) == -1
        )

    # TESTES DAS CONSTRUCOES
    @staticmethod
    def testar_construcoes():
        print("\n--- CONSTRUCOES ---")

        cidade = Testes.nova_cidade()
        construcoes = Construcoes()

        cidade.remover_servos(150)

        resultado = construcoes.recrutar_soldados(
            cidade, 100
        )

        Testes.verificar(
            "Recrutamento sem servos suficientes e recusado",
            not resultado
        )

        Testes.verificar(
            "Recrutamento recusado nao desconta florins",
            cidade.get_florins() == 1000
        )

        resultado = construcoes.construir(cidade, 10)

        Testes.verificar(
            "Construir 10 edificios funciona",
            resultado and cidade.get_construcoes() == 10
        )

        Testes.verificar(
            "Construcoes custam 200 florins",
            cidade.get_florins() == 800
        )

    # TESTES DO JOGADOR E DA NOBREZA
    @staticmethod
    def testar_jogador_e_nobreza():
        print("\n--- JOGADOR E NOBREZA ---")

        cidade = Testes.nova_cidade()
        jogador = cidade.get_dono()
        nobreza = Nobreza()

        Testes.verificar(
            "Jogador comeca como Cavaleiro",
            jogador.get_titulo() == "Cavaleiro"
        )

        Testes.verificar(
            "Prestigio inicial igual a 300",
            nobreza.calcular_prestigio(cidade) == 300
        )

        Testes.verificar(
            "Prestigio inicial nao promove",
            not nobreza.verificar_promocao(cidade)
        )

        cidade.adicionar_construcoes(50)

        resultado = nobreza.verificar_promocao(cidade)

        Testes.verificar(
            "Jogador promovido para Barao",
            resultado and jogador.get_titulo() == "Barão"
        )

        Testes.verificar(
            "Promocao acontece um nivel por vez",
            jogador.get_nivel_titulo() == 1
        )

        while not jogador.eh_monarca():
            jogador.promover()

        Testes.verificar(
            "Nao promove alem de Rei/Rainha",
            not jogador.promover()
        )

    # TESTES DA PARTIDA
    @staticmethod
    def testar_partida():
        print("\n--- PARTIDA ---")

        partida = Partida()
        nobreza = Nobreza()

        bolonha = Cidade("Bolonha", Jogador("Jogador 1"))
        milano = Cidade("Milano", Jogador("Jogador 2"))

        partida.adicionar_cidade(bolonha)
        partida.adicionar_cidade(milano)

        Testes.verificar(
            "Primeiro turno pertence a Bolonha",
            partida.get_cidade_atual() == bolonha
        )

        Testes.verificar(
            "Primeiro turno nao encerra o ano",
            not partida.passar_turno()
        )

        Testes.verificar(
            "Segundo turno pertence a Milano",
            partida.get_cidade_atual() == milano
        )

        Testes.verificar(
            "Ultimo turno encerra o ano",
            partida.passar_turno()
        )

        partida.encerrar_ano(nobreza)

        Testes.verificar(
            "Todas as cidades avancam para 1401",
            bolonha.get_ano_atual() == 1401
            and milano.get_ano_atual() == 1401
        )

        Testes.verificar(
            "Partida nao terminou em 1401",
            not partida.terminou()
        )

        milano.get_dono().promover()

        Testes.verificar(
            "Milano lidera por possuir titulo maior",
            partida.determinar_vencedor(nobreza) == milano
        )

        partida.adicionar_cidade(
            Cidade("Florenca", Jogador("Jogador 3"))
        )

        partida.adicionar_cidade(
            Cidade("Veneza", Jogador("Jogador 4"))
        )

        Testes.verificar(
            "Quinta cidade e recusada",
            not partida.adicionar_cidade(
                Cidade("Roma", Jogador("Jogador 5"))
            )
        )

    # EXECUCAO DOS TESTES
    @staticmethod
    def main():
        Testes.aprovados = 0
        Testes.reprovados = 0

        print("===== TESTES BOLONHA E MILANO =====")

        Testes.testar_cidade()
        Testes.testar_mercado()
        Testes.testar_agricultura()
        Testes.testar_governo()
        Testes.testar_construcoes()
        Testes.testar_jogador_e_nobreza()
        Testes.testar_partida()

        print("\n===== RESULTADO FINAL =====")
        print(
            f"Aprovados: {Testes.aprovados} | "
            f"Reprovados: {Testes.reprovados}"
        )

        if Testes.reprovados > 0:
            raise SystemExit(1)


if __name__ == "__main__":
    Testes.main()
