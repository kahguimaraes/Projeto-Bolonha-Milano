class Jogador:

    TITULOS = [
        "Cavaleiro",
        "Barão",
        "Conde",
        "Marquês",
        "Duque",
        "Rei/Rainha"
    ]

    def __init__(self, nome):
        self._nome = nome
        self._nivel_titulo = 0

    def get_nome(self):
        return self._nome

    def get_titulo(self):
        return self.TITULOS[self._nivel_titulo]

    def get_nivel_titulo(self):
        return self._nivel_titulo

    # Promove o jogador em um nivel
    def promover(self):
        if self.eh_monarca():
            return False

        self._nivel_titulo += 1
        return True

    # Verifica se atingiu o ultimo titulo
    def eh_monarca(self):
        return self._nivel_titulo == len(self.TITULOS) - 1
