class Mercado:

    PRECO_GRAO = 2
    PRECO_TERRA = 1

    def get_preco_grao(self):
        return self.PRECO_GRAO

    def get_preco_terra(self):
        return self.PRECO_TERRA

    # Compra de graos
    def comprar_graos(self, cidade, qtd):
        if qtd <= 0:
            return False

        custo = qtd * self.PRECO_GRAO

        if not cidade.remover_florins(custo):
            return False

        cidade.adicionar_graos(qtd)
        return True

    # Venda de graos
    def vender_graos(self, cidade, qtd):
        if qtd <= 0:
            return False

        if not cidade.remover_graos(qtd):
            return False

        cidade.adicionar_florins(qtd * self.PRECO_GRAO)
        return True

    # Compra de terras
    def comprar_terras(self, cidade, qtd):
        if qtd <= 0:
            return False

        custo = qtd * self.PRECO_TERRA

        if not cidade.remover_florins(custo):
            return False

        cidade.adicionar_terras(qtd)
        return True

    # Venda de terras
    def vender_terras(self, cidade, qtd):
        if qtd <= 0:
            return False

        if not cidade.remover_terras(qtd):
            return False

        cidade.adicionar_florins(qtd * self.PRECO_TERRA)
        return True
