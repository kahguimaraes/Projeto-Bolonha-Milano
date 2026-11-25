class Cidade:

    # Construtor da cidade
    def __init__(self, nome, dono):
        self._nome = nome
        self._dono = dono
        self._ano_atual = 1400

    # Avanca um ano
    def avancar_ano(self):
        self._ano_atual += 1

    # Mostra as informacoes da cidade
    def exibir_status(self):
        print("\n===== STATUS DA CIDADE =====")
        print(f"Cidade: {self._nome}")
        print(f"Governante: {self._dono.get_nome()}")
        print(f"Titulo: {self._dono.get_titulo()}")
        print(f"Ano atual: {self._ano_atual}")
