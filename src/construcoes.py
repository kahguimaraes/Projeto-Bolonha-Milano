class Construcoes:

    PRECO_SOLDADO = 5
    SERVOS_POR_SOLDADO = 1
    PRECO_CONSTRUCAO = 20

    def get_preco_soldado(self):
        return self.PRECO_SOLDADO

    def get_preco_construcao(self):
        return self.PRECO_CONSTRUCAO

    # Recrutamento de soldados no jogo
    def recrutar_soldados(self, cidade, qtd):

        if qtd <= 0:
            return False

        custo = qtd * self.PRECO_SOLDADO
        servos_necessarios = qtd * self.SERVOS_POR_SOLDADO

        # Valida os dois recursos antes de alterar
        if cidade.get_florins() < custo:
            return False

        if cidade.get_servos() < servos_necessarios:
            return False

        cidade.remover_florins(custo)
        cidade.remover_servos(servos_necessarios)
        cidade.adicionar_soldados(qtd)

        return True

    # Construir edificios
    def construir(self, cidade, qtd):

        if qtd <= 0:
            return False

        custo = qtd * self.PRECO_CONSTRUCAO

        if not cidade.remover_florins(custo):
            return False

        cidade.adicionar_construcoes(qtd)

        return True
