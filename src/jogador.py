class Jogador:

    # Construtor do jogador
    def __init__(self, nome):
        self._nome = nome
        self._titulo = "Cavaleiro"

    # Retorna o nome do jogador
    def get_nome(self):
        return self._nome

    # Retorna o titulo de nobreza
    def get_titulo(self):
        return self._titulo
