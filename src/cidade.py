class Cidade:

    ANO_INICIAL = 1400
    FLORINS_INICIAIS = 1000
    TERRAS_INICIAIS = 10000
    GRAOS_INICIAIS = 500

    def __init__(self, nome, dono):
        self._nome = nome
        self._dono = dono
        self._ano_atual = self.ANO_INICIAL
        self._florins = self.FLORINS_INICIAIS
        self._terras = self.TERRAS_INICIAIS
        self._graos = self.GRAOS_INICIAIS

    # Metodos de consulta
    def get_nome(self):
        return self._nome

    def get_dono(self):
        return self._dono

    def get_ano_atual(self):
        return self._ano_atual

    def get_florins(self):
        return self._florins

    def get_terras(self):
        return self._terras

    def get_graos(self):
        return self._graos

    def avancar_ano(self):
        self._ano_atual += 1

    # Controle de florins
    def adicionar_florins(self, qtd):
        if qtd > 0:
            self._florins += qtd

    def remover_florins(self, qtd):
        if qtd < 0 or qtd > self._florins:
            return False

        self._florins -= qtd
        return True

    # Controle de terras
    def adicionar_terras(self, qtd):
        if qtd > 0:
            self._terras += qtd

    def remover_terras(self, qtd):
        if qtd < 0 or qtd > self._terras:
            return False

        self._terras -= qtd
        return True

    # Controle de graos
    def adicionar_graos(self, qtd):
        if qtd > 0:
            self._graos += qtd

    def remover_graos(self, qtd):
        if qtd < 0 or qtd > self._graos:
            return False

        self._graos -= qtd
        return True

    # Mostra o status da cidade
    def exibir_status(self):
        print("\n===== STATUS DA CIDADE =====")
        print(f"Cidade: {self._nome}")
        print(f"Governante: {self._dono.get_nome()}")
        print(f"Titulo: {self._dono.get_titulo()}")
        print(f"Ano atual: {self._ano_atual}")
        print(f"Florins: {self._florins}")
        print(f"Terras: {self._terras} hectares")
        print(f"Graos: {self._graos} unidades")
