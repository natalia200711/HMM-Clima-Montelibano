# Modelo Oculto de Markov (HMM) - Predicción Climática

## Descripción del proyecto

Este proyecto consiste en la implementación de un Modelo Oculto de Markov (Hidden Markov Model - HMM) para simular el comportamiento climático del municipio de Montelíbano, Córdoba.

El sistema utiliza probabilidades para representar los cambios entre diferentes estados climáticos y generar observaciones relacionadas con los niveles de humedad.

La simulación fue realizada durante un período de 30 días utilizando Python y diferentes librerías para el análisis y visualización de resultados.

---

# Objetivo

Aplicar los conceptos de distribuciones de probabilidad mediante la implementación de un Modelo Oculto de Markov capaz de simular el comportamiento climático a partir de observaciones de humedad.

---

# Estados ocultos

Los estados climáticos utilizados en el modelo son:

- Soleado
- Nublado
- Lluvioso

---

# Observaciones

Las observaciones utilizadas corresponden a:

- Humedad Baja
- Humedad Media
- Humedad Alta

---

# Tecnologías y librerías utilizadas

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn

---

# Funcionalidades del programa

El sistema permite:

- Simular el clima durante 30 días.
- Generar observaciones de humedad.
- Mostrar las primeras observaciones del sistema.
- Calcular estadísticas climáticas.
- Generar matriz de confusión.
- Visualizar gráficos climáticos.
- Analizar el comportamiento probabilístico del modelo.

---

# Estructura del repositorio

```text
HMM-Clima-Montelibano
│
├── codigo
│   └── Cabrera_Natalia_Markov.py
│
├── evidencias
│   ├── relacion_estados_observaciones.png
│   ├── estados_climaticos.png
│   ├── observaciones_humedad.png
│   └── graficos_alineados.png
│
└── README.md
```

---

# Instrucciones de ejecución

## 1. Clonar el repositorio

```bash
git clone https://github.com/natalia200711/HMM-Clima-Montelibano.git
```

---

## 2. Instalar las librerías necesarias

```bash
pip install numpy pandas matplotlib seaborn
```

---

## 3. Ejecutar el programa

Abrir el archivo Python en:

- Visual Studio Code
- Jupyter Notebook
- Google Colab

Luego ejecutar el archivo principal.

---

# Resultados obtenidos

Durante la simulación se logró representar el comportamiento probabilístico del clima mediante estados ocultos y observaciones visibles.

Los resultados permitieron analizar cómo cambian las condiciones climáticas a través del tiempo utilizando probabilidades de transición y emisión.

---

# Autor

Natalia Cabrera Anaya
