# Reporte del Modelo Baseline

Este documento contiene los resultados del modelo baseline realizado con regresión logística.

## Descripción del modelo

El modelo baseline es el primer modelo construido y se utiliza para establecer una línea base para el rendimiento de los modelos posteriores. Se emplea para esto un modelo de regresión logística, el cual busca clasificar los datos de forma binaria en dos categorías ($0$ y $1$). Para ello, usa la función logística o sigmoidal:

$$
\hat{y} = \frac{1}{1+e^{-\mathbf{w}\cdot\mathbf{x}+w_0}}
$$

Como hiperparámetros del modelo se examina el comportamiento del parámetro "C": inversa de la fortaleza de regularización, con valores entre 0.0001 y 10 en escala logarítmica y "solver", el algoritmo empleado en la optimización del problema, con valores: "lbfgs", "liblinear", "newton-cg", "newton-cholesky", "sag" y "saga". La optimización de parámetros se realizó con *Optuna* buscando maximizar la métrica F1 con 1000 ensayos.

## Variables de entrada

Las variables de entrada que se emplearon son: 
- Las variables numéricas "time", "age, "wtkg", "preanti", "cd40", "dif_cd4", "cd80" y "dif_cd8".
- Las variables categóricas "karnof_encoded", "hemo", "drugs", "race", "gender, "symptom", "treat" y "offtrt".
Las varibles numéricas se escalaron con *StandardScaler* de *Sklearn*. La variable "karnof_encoded" es el ajuste de la variable original "karnof" con "OrdinalScaler". Las demás variables son categóricas binarias.

## Variable objetivo

La etiqueta del problema es la varible binaria "infected".

## Cantidad de observaciones
El archivo original contiene 2139 entradas. Se realizó la separación en datos de entranamiento y datos de prueba dejando un 25% del total de datos para prueba. Ya que la etiqueta está desbalanceada, se empleó *SMOTE* para que los datos en el conjunto de prueba quedasen balanceados. De esta manera hay 2414 observaciones para entrenamiento y 535 para prueba.

## Evaluación del modelo

### Métricas de evaluación

Descripción de las métricas utilizadas para evaluar el rendimiento del modelo.

### Resultados de evaluación

| Tipo de modelo | Mejores hiperparámetros | Exactitud (*Accuracy*) | Métrica F1 | 
| --- | --- | --- | --- | 
| Regresión logística | 'C': 0.08011117642517443, 'solver': 'lbfgs' | 0.8448598130841122 | 0.6937269372693727 |


## Análisis de los resultados

La exactitud del modelo, aunque no es mala, da un amplio margen de mejora.

## Conclusiones

Se pueden desarrollar otros modelos para mejorar el resultado acá encontrado.

## Referencias

Lista de referencias utilizadas para construir el modelo baseline y evaluar su rendimiento.

Espero que te sea útil esta plantilla. Recuerda que puedes adaptarla a las necesidades específicas de tu proyecto.
