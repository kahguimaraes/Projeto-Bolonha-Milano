class Nobreza:

    PESO_CONSTRUCAO = 10
    PESO_SOLDADO = 2
    PESO_SERVO = 1
    HECTARES_POR_PONTO = 100

    PRESTIGIO_MINIMO = [0, 400, 550, 700, 850, 1000]

    # Calcula o prestigio da cidade
    def calcular_prestigio(self, cidade):
        return (
            cidade.get_construcoes() * self.PESO_CONSTRUCAO
            + cidade.get_soldados() * self.PESO_SOLDADO
            + cidade.get_servos() * self.PESO_SERVO
            + cidade.get_terras() // self.HECTARES_POR_PONTO
        )

    # Retorna o prestigio necessario para o proximo titulo
    def prestigio_para_proximo_titulo(self, jogador):
        if jogador.eh_monarca():
            return -1

        proximo = jogador.get_nivel_titulo() + 1

        return self.PRESTIGIO_MINIMO[proximo]

    # Verifica se o jogador pode ser promovido
    def verificar_promocao(self, cidade):
        jogador = cidade.get_dono()

        necessario = self.prestigio_para_proximo_titulo(
            jogador
        )

        if necessario == -1:
            return False

        prestigio = self.calcular_prestigio(cidade)

        if prestigio >= necessario:
            return jogador.promover()

        return False
