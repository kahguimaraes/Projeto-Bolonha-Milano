class Governo:

    TAXA_MAXIMA = 50
    MULTIPLICADOR_JUSTA = 0.8
    MULTIPLICADOR_MODERADA = 1.0
    MULTIPLICADOR_SEVERA = 1.3

    def arrecadar_impostos(self, cidade):

        # Permite apenas uma arrecadacao por ano
        if cidade.is_impostos_arrecadados():
            return -1

        base = (
            cidade.get_servos()
            * cidade.get_taxa_imposto() // 100
        )

        multiplicador = self.multiplicador_para(
            cidade.get_nivel_justica()
        )

        arrecadado = int(base * multiplicador)

        cidade.adicionar_florins(arrecadado)

        cidade.marcar_impostos_arrecadados()

        return arrecadado

    def definir_taxa_imposto(self, cidade, taxa):

        if not 0 <= taxa <= self.TAXA_MAXIMA:
            return False

        cidade.set_taxa_imposto(taxa)

        return True

    def definir_justica(self, cidade, nivel):

        nivel = nivel.strip().capitalize()

        if nivel not in ("Justa", "Moderada", "Severa"):
            return False

        cidade.set_nivel_justica(nivel)

        return True

    def multiplicador_para(self, nivel):

        if nivel == "Justa":
            return self.MULTIPLICADOR_JUSTA

        elif nivel == "Severa":
            return self.MULTIPLICADOR_SEVERA

        return self.MULTIPLICADOR_MODERADA
