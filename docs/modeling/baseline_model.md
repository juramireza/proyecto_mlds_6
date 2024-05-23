# Reporte del Modelo Baseline

Este documento contiene los resultados del modelo baseline realizado con el algoritmo de regresión logística.

## Descripción del modelo

<p align="justify">
El modelo baseline es el primer modelo construido y se utiliza para establecer una línea base para el rendimiento de los modelos posteriores. Se empleó para esto el algoritmo de regresión logística, el cual busca clasificar los datos de forma binaria en dos categorías ($0$ y $1$). Para ello, usa la función logística o sigmoidal:
</p>

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

<p align="justify">
La etiqueta del problema es la varible binaria "infected", que es la variable dependiente y la que indica si un paciente tiene el virus del VIH (SIDA)
</p>

## Cantidad de observaciones

<p align="justify">
El archivo original contiene 2139 entradas. Se realizó la separación en datos de entranamiento y datos de prueba dejando un 25% del total de datos para prueba. Ya que la etiqueta está desbalanceada, se empleó *SMOTE* para que los datos en el conjunto de prueba quedasen balanceados. De esta manera hay 2414 observaciones para entrenamiento y 535 para prueba.

</p>

## Evaluación del modelo

### Métricas de evaluación

<p align="justify">
En los modelos empleados se observó el comportamiento de dos métricas apropiadas para clasificación binaria:

</p>

- *Exactitud*: mide cuantitativamente cuantas predicciones fueron correctas.
- *Recall*: Proporción de verdaderos positivos entre los positivos reales.
- *Precisión*: es la habilidad del clasificador de no clasificar una muestra como positiva cuando es negativa.
- *F1 score*: El F1 score es la media armónica de la precisión y el recall. Un F1 score alto indica un buen equilibrio entre precisión y exhaustividad.

### Resultados de evaluación

| Tipo de modelo | Mejores hiperparámetros | Exactitud (*Accuracy*) |  F1 Score | 
| --- | --- | --- | --- | 
| Regresión logística | 'C': 0.08011117642517443, 'solver': 'lbfgs' | 0.8448598130841122 | 0.6937269372693727 |


## Análisis de los resultados

La exactitud del modelo del modelo es de 0.84, que es un valor que a primera vista parece bastante bueno, pero al revisar el valor del F1 Score es de 0.69, esto indica que la calidad del modelo no es tan alta, ya que, hay presencia de Falsos positivos y/o de Falsos negativos. 

## Conclusiones

- Con el algoritmo de regresión logística, se consiguen resultados consistentes, aunque con oportunidad de mejora, ya que, el valor del F1-Score es relativamente bajo (0.69).

##Recomendaciones 

A continuación, se presentan algunas sugerencias, con el fin de construir un modelo que consiga mejores resultados: 

- Experimentar con algoritmos diferentes al de la regresión logística. 
- Revisar aquellas observaciones que están siendo mal clasificadas e intentar comprender esto porque sucede. 
- Iterar en el proceso completo, es decir revisar el análisis exploratorio y ver que variables valdría la pena incluir y que variables, es mejor excluir. 
- En caso de ser viable, conseguir más observaciones con el fin de aumentar el conjunto de datos. 
- Si existe la posibilidad, explorar nuevas variables. 

## Referencias

[Regresión logística en SciKitLearn](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html).
