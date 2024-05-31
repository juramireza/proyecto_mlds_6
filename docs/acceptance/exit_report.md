# Informe de salida

## Resumen Ejecutivo

<p align="justify">

Este informe describe los resultados obtenidos con el proyecto "Modelo de predictivo basado en aprendizaje de máquina para la detección del SIDA (VIH) con base en información clínica y sociodemográfica" y presenta tanto los principales logros como las lecciones aprendidas durante el proceso.

</p>


## Resultados del proyecto

1. Resumen de los entregables y logros alcanzados en cada etapa del proyecto:

<p align="justify">

- Business Understanding y Data Understading: En esta etapa se realizó un entendimiento de algunas variables clínicas y sociodemográficas asociadas con la prescripción del VIH (SIDA) en pacientes. Y se hizo la entrega de un diccionario de datos de las variables del conjunto de datos. 
</p>

<p align="justify">

- Data Preparation: En este paso, se hizo un análisis exploratorio de los datos, se reviso la distribución de la variable dependiente, donde se apreció que los datos estaban desbalanceados, ya que, se tenían más observaciones de pacientes no infectados que de infectados, en una proporción de de tres a uno, con base en esto, se aplico la técnica de smote, para construir un conjunto de datos balanceado. Y también, se seleccionaron las variables, con mayor grado de influencia para conseguir el objetivo de predecir, si un paciente tiene VIH(SIDA) o no. Entonces, en esta etapa se logró, construir un conjunto de datos balanceado, con las variables de mayor influencia, para predecir la variable dependiente (infected).
</p>

<p align="justify">

- Modeling: En esta parte, se utilizaron siete algoritmos en conjunto, con la herramienta optuna para conseguir los mejores hiperparámetros con cada uno de los algoritmos y elaborar los mejores modelos. De esta etapa, se obtuvieron siete modelos.

</p>

<p align="justify">

- Evaluation: En este apartado, utilizando la matriz de confusión, y las métricas tanto de exactitud como de F1-Score, que se derivan de esta. Se evaluaron y compararon, los siete modelos, apreciando que los mejores resultados se lograron con el algoritmo de bosques aleatorios. 

</p>




- Evaluación del modelo final y comparación con el modelo base.
- Descripción de los resultados y su relevancia para el negocio.

## Lecciones aprendidas

- Identificación de los principales desafíos y obstáculos encontrados durante el proyecto.
- Lecciones aprendidas en relación al manejo de los datos, el modelamiento y la implementación del modelo.
- Recomendaciones para futuros proyectos de machine learning.

## Impacto del proyecto

- Descripción del impacto del modelo en el negocio o en la industria.
- Identificación de las áreas de mejora y oportunidades de desarrollo futuras.

## Conclusiones

- Resumen de los resultados y principales logros del proyecto.
- Conclusiones finales y recomendaciones para futuros proyectos.

## Agradecimientos

- Agradecimientos al equipo de trabajo y a los colaboradores que hicieron posible este proyecto.
- Agradecimientos especiales a los patrocinadores y financiadores del proyecto.
