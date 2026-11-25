class Partida:

    MAXIMO_JOGADORES = 4
    ANO_FINAL = 1410

    def __init__(self):
        self._cidades = []
        self._indice_atual = 0

    # Adiciona uma cidade na partida
    def adicionar_cidade(self, cidade):
        if len(self._cidades) >= self.MAXIMO_JOGADORES:
            return False

        self._cidades.append(cidade)
        return True

    def get_cidades(self):
        return self._cidades

    def get_cidade_atual(self):
        if not self._cidades:
            return None

        return self._cidades[self._indice_atual]

    def get_ano_atual(self):
        if not self._cidades:
            return 1400

        return self._cidades[0].get_ano_atual()

    def get_ano_final(self):
        return self.ANO_FINAL

    # Passa a vez para o proximo jogador
    def passar_turno(self):
        if not self._cidades:
            return False

        self._indice_atual += 1

        if self._indice_atual >= len(self._cidades):
            self._indice_atual = 0
            return True

        return False

    # Avanca o ano e verifica as promocoes
    def encerrar_ano(self, nobreza):
        promovidas = []

        for cidade in self._cidades:
            cidade.avancar_ano()

            if nobreza.verificar_promocao(cidade):
                promovidas.append(cidade)

        return promovidas

    # Verifica se a partida terminou
    def terminou(self):
        if not self._cidades:
            return False

        for cidade in self._cidades:
            if cidade.get_dono().eh_monarca():
                return True

        return self.get_ano_atual() > self.ANO_FINAL

    # Determina o vencedor
    def determinar_vencedor(self, nobreza):
        if not self._cidades:
            return None

        return max(
            self._cidades,
            key=lambda cidade: (
                cidade.get_dono().get_nivel_titulo(),
                nobreza.calcular_prestigio(cidade)
            )
        )
