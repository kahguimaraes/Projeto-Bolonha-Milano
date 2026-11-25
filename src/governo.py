class Governo:

    TAXA_MAXIMA = 50
    MULTIPLICADOR_JUSTA = 0.8
    MULTIPLICADOR_MODERADA = 1.0
    MULTIPLICADOR_SEVERA = 1.3

    # Calcula e arrecada os impostos
    def arrecadar_impostos(self, cidade):

        base = (
            cidade.get_servos() *
            cidade.get_taxa_imposto() // 100
        )

        multiplicador = self.multiplicador_para(
            cidade.get_nivel_justica()
        )

        arrecadado = int(base * multiplicador)

        cidade.adicionar_florins(arrecadado)

        return arrecadado

    # Define a taxa de imposto
    def definir_taxa_imposto(self, cidade, taxa):

        if not 0 <= taxa <= self.TAXA_MAXIMA:
            return False

        cidade.set_taxa_imposto(taxa)

        return True

    # Define o nivel de justica
    def definir_justica(self, cidade, nivel):

        nivel = nivel.strip().capitalize()

        if nivel not in ("Justa", "Moderada", "Severa"):
            return False

        cidade.set_nivel_justica(nivel)

        return True

    # Retorna o multiplicador de justica
    def multiplicador_para(self, nivel):

        if nivel == "Justa":
            return self.MULTIPLICADOR_JUSTA

        elif nivel == "Severa":
            return self.MULTIPLICADOR_SEVERA

        return self.MULTIPLICADOR_MODERADA
