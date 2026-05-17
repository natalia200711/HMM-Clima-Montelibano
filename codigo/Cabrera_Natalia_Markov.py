# ----------------------------------------------------------
# IMPORTACIÓN DE LIBRERÍAS
# ----------------------------------------------------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------------------------------------
# CONFIGURACIÓN VISUAL
# ----------------------------------------------------------

plt.style.use('ggplot')

# ----------------------------------------------------------
# CLASE HIDDEN MARKOV MODEL
# ----------------------------------------------------------

class HiddenMarkovModel:

    def __init__(self):

        # --------------------------------------------------
        # ESTADOS OCULTOS DEL CLIMA
        # --------------------------------------------------

        self.estados = [
            'Soleado',
            'Nublado',
            'Lluvioso'
        ]

        # --------------------------------------------------
        # OBSERVACIONES DE HUMEDAD
        # --------------------------------------------------

        self.observaciones = [
            'Humedad Baja',
            'Humedad Media',
            'Humedad Alta'
        ]

        # --------------------------------------------------
        # DISTRIBUCIÓN INICIAL
        # --------------------------------------------------

        self.distribucion_inicial = [
            0.6,
            0.3,
            0.1
        ]

        # --------------------------------------------------
        # MATRIZ DE TRANSICIÓN
        # --------------------------------------------------

        self.matriz_transicion = np.array([
            [0.7, 0.2, 0.1],
            [0.3, 0.4, 0.3],
            [0.2, 0.3, 0.5]
        ])

        # --------------------------------------------------
        # MATRIZ DE EMISIÓN
        # --------------------------------------------------

        self.matriz_emision = np.array([
            [0.7, 0.2, 0.1],
            [0.2, 0.5, 0.3],
            [0.1, 0.3, 0.6]
        ])

        # --------------------------------------------------
        # COLORES PARA LOS ESTADOS CLIMÁTICOS
        # --------------------------------------------------

        self.colores_estados = {
            'Soleado': '#FFD700',   # Amarillo
            'Nublado': '#87CEEB',   # Azul claro
            'Lluvioso': '#1E3A5F'   # Azul oscuro
        }

        # --------------------------------------------------
        # COLORES PARA LAS OBSERVACIONES
        # --------------------------------------------------

        self.colores_humedad = {
            'Humedad Baja': '#F4E285',
            'Humedad Media': '#7BDFF2',
            'Humedad Alta': '#3D5A80'
        }

    # ------------------------------------------------------
    # FUNCIÓN PARA SIMULAR EL CLIMA
    # ------------------------------------------------------

    def simular(self, dias=30):

        estados_generados = []
        observaciones_generadas = []

        # Estado inicial aleatorio
        estado_actual = np.random.choice(
            self.estados,
            p=self.distribucion_inicial
        )

        # Simulación día por día
        for dia in range(dias):

            estados_generados.append(
                estado_actual
            )

            # Índice del estado actual
            indice_estado = self.estados.index(
                estado_actual
            )

            # Generar observación de humedad
            observacion = np.random.choice(
                self.observaciones,
                p=self.matriz_emision[indice_estado]
            )

            observaciones_generadas.append(
                observacion
            )

            # Generar siguiente estado climático
            estado_actual = np.random.choice(
                self.estados,
                p=self.matriz_transicion[indice_estado]
            )

        return estados_generados, observaciones_generadas

    # ------------------------------------------------------
    # MOSTRAR LOS PRIMEROS 10 DÍAS
    # ------------------------------------------------------

    def mostrar_primeros_dias(
        self,
        estados,
        observaciones
    ):

        print("\n=================================================")
        print("              PRIMEROS 10 DÍAS")
        print("=================================================\n")

        for i in range(10):

            print(
                f"Día {i+1:02d}: "
                f"{estados[i]} → "
                f"{observaciones[i]}"
            )

    # ------------------------------------------------------
    # CALCULAR ESTADÍSTICAS
    # ------------------------------------------------------

    def calcular_estadisticas(
        self,
        estados,
        observaciones
    ):

        print("\n=================================================")
        print("                 ESTADÍSTICAS")
        print("=================================================\n")

        # --------------------------------------------------
        # DÍAS POR ESTADO CLIMÁTICO
        # --------------------------------------------------

        conteo_estados = pd.Series(
            estados
        ).value_counts()

        print("DÍAS POR ESTADO CLIMÁTICO:\n")

        for estado, cantidad in conteo_estados.items():

            print(
                f"{estado}: {cantidad} días"
            )

        # --------------------------------------------------
        # PORCENTAJE DE HUMEDAD
        # --------------------------------------------------

        conteo_humedad = (
            pd.Series(observaciones)
            .value_counts(normalize=True) * 100
        )

        print("\n")
        print("PORCENTAJE DE HUMEDAD OBSERVADA:\n")

        for humedad, porcentaje in conteo_humedad.items():

            print(
                f"{humedad}: "
                f"{porcentaje:.2f}%"
            )

        # --------------------------------------------------
        # MOSTRAR PARÁMETROS DEL MODELO
        # --------------------------------------------------

        print("\n")
        print("PROBABILIDADES INICIALES:\n")

        for estado, probabilidad in zip(
            self.estados,
            self.distribucion_inicial
        ):

            print(
                f"{estado}: "
                f"{probabilidad}"
            )

        print("\n")
        print("MATRIZ DE TRANSICIÓN:\n")

        print(
            pd.DataFrame(
                self.matriz_transicion,
                index=self.estados,
                columns=self.estados
            )
        )

        print("\n")
        print("MATRIZ DE EMISIÓN:\n")

        print(
            pd.DataFrame(
                self.matriz_emision,
                index=self.estados,
                columns=self.observaciones
            )
        )

    # ------------------------------------------------------
    # MATRIZ DE CONFUSIÓN
    # ------------------------------------------------------

    def matriz_confusion(
        self,
        estados,
        observaciones
    ):

        tabla = pd.crosstab(
            pd.Series(
                estados,
                name='Estado'
            ),
            pd.Series(
                observaciones,
                name='Observación'
            )
        )

        print("\n=================================================")
        print("             MATRIZ DE CONFUSIÓN")
        print("=================================================\n")

        print(tabla)

        # --------------------------------------------------
        # HEATMAP
        # --------------------------------------------------

        plt.figure(figsize=(8, 5))

        sns.heatmap(
            tabla,
            annot=True,
            cmap='Blues',
            fmt='d',
            linewidths=1
        )

        plt.title(
            'Relación entre Estados y Observaciones',
            fontsize=14,
            fontweight='bold'
        )

        plt.tight_layout()

        plt.show(block=False)

    # ------------------------------------------------------
    # GRÁFICO DE ESTADOS CLIMÁTICOS
    # ------------------------------------------------------

    def graficar_estados(
        self,
        estados
    ):

        plt.figure(figsize=(15, 5))

        for i, estado in enumerate(estados):

            plt.bar(
                i,
                1,
                color=self.colores_estados[estado]
            )

        plt.title(
            'Secuencia de Estados Climáticos '
            '- Montelíbano',
            fontsize=15,
            fontweight='bold'
        )

        plt.xlabel('Días')
        plt.yticks([])

        plt.grid(
            axis='x',
            linestyle='--',
            alpha=0.3
        )

        plt.tight_layout()

        plt.show(block=False)

    # ------------------------------------------------------
    # GRÁFICO DE OBSERVACIONES
    # ------------------------------------------------------

    def graficar_observaciones(
        self,
        observaciones
    ):

        plt.figure(figsize=(15, 5))

        for i, observacion in enumerate(observaciones):

            plt.bar(
                i,
                1,
                color=self.colores_humedad[
                    observacion
                ]
            )

        plt.title(
            'Observaciones de Humedad',
            fontsize=15,
            fontweight='bold'
        )

        plt.xlabel('Días')
        plt.yticks([])

        plt.grid(
            axis='x',
            linestyle='--',
            alpha=0.3
        )

        plt.tight_layout()

        plt.show(block=False)

    # ------------------------------------------------------
    # GRÁFICOS ALINEADOS TEMPORALMENTE
    # ------------------------------------------------------

    def graficos_combinados(
        self,
        estados,
        observaciones
    ):

        fig, axs = plt.subplots(
            2,
            1,
            figsize=(16, 8),
            sharex=True
        )

        # --------------------------------------------------
        # ESTADOS CLIMÁTICOS
        # --------------------------------------------------

        for i, estado in enumerate(estados):

            axs[0].bar(
                i,
                1,
                color=self.colores_estados[estado]
            )

        axs[0].set_title(
            'Estados Climáticos',
            fontsize=14,
            fontweight='bold'
        )

        axs[0].set_yticks([])

        # --------------------------------------------------
        # OBSERVACIONES DE HUMEDAD
        # --------------------------------------------------

        for i, observacion in enumerate(
            observaciones
        ):

            axs[1].bar(
                i,
                1,
                color=self.colores_humedad[
                    observacion
                ]
            )

        axs[1].set_title(
            'Observaciones de Humedad',
            fontsize=14,
            fontweight='bold'
        )

        axs[1].set_yticks([])

        plt.xlabel('Días')

        plt.tight_layout()

        plt.show(block=False)

    # ------------------------------------------------------
    # REPORTE FINAL
    # ------------------------------------------------------

    def reporte_final(
        self,
        estados
    ):

        estado_dominante = max(
            set(estados),
            key=estados.count
        )

        print("\n=================================================")
        print("                 REPORTE FINAL")
        print("=================================================\n")

        print(
            "Municipio analizado: "
            "Montelíbano - Córdoba"
        )

        print(
            f"Estado climático predominante: "
            f"{estado_dominante}"
        )

        if estado_dominante == 'Soleado':

            print(
                "\nConclusión:"
            )

            print(
                "Durante la simulación climática "
                "predominaron los días soleados, "
                "lo que indica un comportamiento "
                "climático estable y seco."
            )

        elif estado_dominante == 'Nublado':

            print(
                "\nConclusión:"
            )

            print(
                "El clima presentó condiciones "
                "variables con presencia frecuente "
                "de nubosidad."
            )

        else:

            print(
                "\nConclusión:"
            )

            print(
                "La simulación mostró una alta "
                "presencia de lluvia y humedad."
            )

# ----------------------------------------------------------
# PROGRAMA PRINCIPAL
# ----------------------------------------------------------

if __name__ == "__main__":

    print("\n=================================================")

    print(
        " MODELO OCULTO DE MARKOV "
        "- PREDICCIÓN CLIMÁTICA "
    )

    print(
        " MUNICIPIO DE "
        "MONTELÍBANO "
    )

    print("=================================================\n")

    # ------------------------------------------------------
    # CREAR MODELO
    # ------------------------------------------------------

    modelo = HiddenMarkovModel()

    # ------------------------------------------------------
    # SIMULACIÓN DE 30 DÍAS
    # ------------------------------------------------------

    estados, observaciones = modelo.simular(
        dias=30
    )

    # ------------------------------------------------------
    # MOSTRAR RESULTADOS
    # ------------------------------------------------------

    modelo.mostrar_primeros_dias(
        estados,
        observaciones
    )

    modelo.calcular_estadisticas(
        estados,
        observaciones
    )

    modelo.matriz_confusion(
        estados,
        observaciones
    )

    modelo.graficar_estados(
        estados
    )

    modelo.graficar_observaciones(
        observaciones
    )

    modelo.graficos_combinados(
        estados,
        observaciones
    )

    modelo.reporte_final(
        estados
    )

    # ------------------------------------------------------
    # MANTENER TODAS LAS GRÁFICAS ABIERTAS
    # ------------------------------------------------------

    plt.show()