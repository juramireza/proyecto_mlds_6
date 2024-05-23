# Reporte de modelos desarrollados

<p align="justify">
Este documento contiene los resultados de los mejores modelos que se construyeron utilizando distintos tipos de algoritmos.
</p>

# Variables y observaciones

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
El archivo original contiene 2139 entradas. Se realizó la separación en datos de entranamiento y datos de prueba dejando un 25% del total de datos para prueba. Ya que la etiqueta está desbalanceada, se empleó *SMOTE* para que los datos en el conjunto de prueba quedasen distribuidos de forma equitativa. De esta manera hay 2414 observaciones para entrenamiento y 535 para prueba.
</p>

# Algoritmos utilizados en la construcción de los modelos


## Regresión logística

<p align="justify">
La regresión logística es un algoritmo paramétrico que clasifica datos binarios convirtiendo una combinación lineal de características en probabilidades usando la función sigmoide. Predice la clase basándose en si la probabilidad supera un umbral (típicamente 0.5)
</p>


## Bosque aleatorio

<p align="justify">
El clasificador de bosque aleatorio consiste en una colección de árboles de decisión entrenados en muestras distintas que realizan una "votación" para elegir la clasificación más favorable. La cantidad de árboles que se entrenan se define con el parámetro ```n_estimators```, y se pueden configurar los parámetros de estos árboles, como por ejemplo la cantidad máxima de características a considerar con ```max_features```. (Tomado del material de estudio de módulo 2).
</p>

## Máquinas de soporte vectorial

<p align="justify">
Las máquinas de soporte vectorial (SVM) son algoritmos de clasificación que encuentran el hiperplano que mejor separa las clases de datos en un espacio de características. 
</p>

## k-NN (k-Nearest Neighbors) 
<p align="justify">
El algoritmo k-NN (k-Nearest Neighbors) clasifica una observación basándose en las clases de sus k vecinos más cercanos en el espacio de características.
</p>

## Métricas de evaluación

<p align="justify">
En los modelos empleados se observó el comportamiento de dos métricas apropiadas para clasificación binaria:

</p>

- *Exactitud*: mide cuantitativamente cuantas predicciones fueron correctas.
- *Recall*: Proporción de verdaderos positivos entre los positivos reales.
- *Precisión*: es la habilidad del clasificador de no clasificar una muestra como positiva cuando es negativa.
- *F1 score*: El F1 score es la media armónica de la precisión y el recall. Un F1 score alto indica un buen equilibrio entre precisión y exhaustividad.

### Resultados de evaluación

| Tipo de algoritmo | Mejores hiperparámetros | Exactitud (*Accuracy*) | F1 Score| 
| --- | --- | --- | --- | 
| Regresión logística | 'C': 0.08011117642517443, 'solver': 'lbfgs' | 0.8448598130841122 | 0.6937269372693727 |
| Bosques aleatorios | 'n_estimators': 73, 'criterion': 'gini', 'max_depth': 50, 'min_samples_split': 20, 'min_samples_leaf': 2, 'min_weight_fraction_leaf': 2.5214105645479093e-05, 'ccp_alpha': 1.8151142421551003e-05, 'max_samples': 0.959999447846922 | 0.8710280373831776 | 0.7544483985765125 |
| SVM | 'C': 2.7807647750443065,'break_ties': False,'cache_size': 200,'class_weight': None,'coef0': 0.0,'decision_function_shape': 'ovr','degree': 3,'gamma': 'scale','kernel': 'rbf', 'max_iter': -1, 'probability': False,'random_state': None,'shrinking': True, 'tol': 0.001,'verbose': False |  0.8635514018691589 | 0.7224334600760456 |
| k-NN |'algorithm': 'auto','leaf_size': 80,'metric': 'minkowski','metric_params': None 'n_jobs': None,'n_neighbors': 20,'p': 1,'weights': 'uniform'| 0.8317757009345794 | 0.6785714285714285 |

## Análisis de los resultados

<p align="justify">
Con el algoritmo de bosques aleatorios, se consiguen los mejores resultados. Ya que, con este se consiguen los valores más altos tanto de Exactitud (0.87) como de F1 Score (0.75). Esto, significa que es el modelo, que más observaciones ha conseguido clasificar correctamente y el que logra un mejor balance entre precisión y exhaustividad.
</p>

<p align="justify">
El algoritmo de máquinas de soporte vectorial, arroja resultados inferiores que el de Bosques Alatorios, con una Exactitud de 0.86 y un F1 Score de 0.72. Pero, con estas métricas tiene mejor desempeño, que los modelos obtenidos con los algoritmos de k-NN y Regresión logística. 

<p align="justify">
Por último, el modelo construído con el algoritmo de regresión logística registro una Exactitud de 0.84 y un F1 Score de 0.69, métricas inferiores a las obtenidas tanto con Bosques aleatorios como con SVM, pero superiores a las que se lograron al aplicar el algoritmo de k-NN. Es decir, el modelo con las peores métricas fue este, con una Exactitud de 0.83 y un F1 Score de 0.67.
</p>


## Conclusiones

<p align="justify">

- Con el algoritmo de bosques aleatorios, se consiguen los mejores resultados. Ya que, con este se consiguen los valores más altos tanto de Exactitud (0.87) como de F1 Score (0.75), después se tiene el modelo construido con el algoritmo de SVM, con una Exactitud de 0.86 y un F1 Score de 0.72, luego esta el modelo elaborado con el algoritmo de regresión logística con una Exactitud de 0.84 y un F1 Score de 0.69. Y por último, siendo el modelo con peores métricas, se encuentra el que se desarrollo con el algoritmo de k-NN, con una Exactitud de 0.83 y un F1 Score de 0.67. 
</p>

## Recomendaciones 

A continuación, se presentan algunas sugerencias, con el fin de construir un modelo que consiga mejores resultados: 

- Experimentar con algoritmos diferentes al de la regresión logística. 
- Revisar aquellas observaciones que están siendo mal clasificadas e intentar comprender esto porque sucede. 
- Iterar en el proceso completo, es decir revisar el análisis exploratorio y ver que variables valdría la pena incluir y que variables, es mejor excluir. 
- En caso de ser viable, conseguir más observaciones con el fin de aumentar el conjunto de datos. 
- Si existe la posibilidad, explorar nuevas variables. 

## Referencias

[Bosque aleatrorio en SciKitLearn](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)

[Regresión logística en SciKitLearn](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html).


[svm](https://scikit-learn.org/stable/modules/svm.html).

[k-NN](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html).

