class Agricultura:

    HECTARES_POR_SERVO = 5
    RENDIMENTO_POR_HECTARE = 2
    SERVOS_POR_GRAO = 5
    CRESCIMENTO_PERCENTUAL = 5
    PERCENTUAL_MINIMO = 20
    PERCENTUAL_MAXIMO = 80

    def processar_colheita(self, cidade):

        # Permite apenas uma colheita por ano
        if cidade.is_colheita_feita():
            return -1

        hectares = min(
            cidade.get_terras(),
            cidade.get_servos() * self.HECTARES_POR_SERVO
        )

        sementes = hectares // 2

        if sementes > cidade.get_graos():
            sementes = cidade.get_graos()
            hectares = sementes * 2

        cidade.remover_graos(sementes)

        producao = hectares * self.RENDIMENTO_POR_HECTARE

        cidade.adicionar_graos(producao)

        cidade.marcar_colheita_feita()

        print("\n===== RESULTADO DA COLHEITA =====")
        print(f"Hectares cultivados: {hectares}")
        print(f"Sementes utilizadas: {sementes}")
        print(f"Graos produzidos: {producao}")
        print(f"Estoque atual: {cidade.get_graos()}")

        return hectares

    def distribuir_alimentos(self, cidade, percentual):

        if not self.PERCENTUAL_MINIMO <= percentual <= self.PERCENTUAL_MAXIMO:
            return False

        alimento = cidade.get_graos() * percentual // 100

        cidade.remover_graos(alimento)

        necessidade = cidade.get_servos() // self.SERVOS_POR_GRAO

        print("\n===== DISTRIBUICAO DE ALIMENTOS =====")
        print(f"Alimentos distribuidos: {alimento}")
        print(f"Necessidade da populacao: {necessidade}")

        if alimento >= necessidade:
            crescimento = (
                cidade.get_servos()
                * self.CRESCIMENTO_PERCENTUAL // 100
            )

            cidade.adicionar_servos(crescimento)

            print(f"Crescimento populacional: {crescimento}")

        else:
            deficit = necessidade - alimento
            perda = min(deficit, cidade.get_servos())

            cidade.remover_servos(perda)

            print(f"Reducao populacional: {perda}")

        print(f"Populacao atual: {cidade.get_servos()}")
        print(f"Estoque de graos: {cidade.get_graos()}")

        return True
