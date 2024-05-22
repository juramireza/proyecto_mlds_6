# Reporte del otros modelos desarrollados

Este documento contiene los resultados del otros modelos.

# Variables y observaciones

## Variables de entrada

Las variables de entrada que se emplearon son: 
- Las variables numéricas "time", "age, "wtkg", "preanti", "cd40", "dif_cd4", "cd80" y "dif_cd8".
- Las variables categóricas "karnof_encoded", "hemo", "drugs", "race", "gender, "symptom", "treat" y "offtrt".
Las varibles numéricas se escalaron con *StandardScaler* de *Sklearn*. La variable "karnof_encoded" es el ajuste de la variable original "karnof" con "OrdinalScaler". Las demás variables son categóricas binarias.

## Variable objetivo

La etiqueta del problema es la varible binaria "infected".

## Cantidad de observaciones
El archivo original contiene 2139 entradas. Se realizó la separación en datos de entranamiento y datos de prueba dejando un 25% del total de datos para prueba. Ya que la etiqueta está desbalanceada, se empleó *SMOTE* para que los datos en el conjunto de prueba quedasen balanceados. De esta manera hay 2414 observaciones para entrenamiento y 535 para prueba.

# Modelos

## Bosque aleatorio

El clasificador de bosque aleatorio consiste en una colección de árboles de decisión entrenados en muestras distintas que realizan una "votación" para elegir la clasificación más favorable. La cantidad de árboles que se entrenan se define con el parámetro ```n_estimators```, y se pueden configurar los parámetros de estos árboles, como por ejemplo la cantidad máxima de características a considerar con ```max_features```. (Tomado del material de estudio de módulo 2).

### Métricas de evaluación

En los modelos empleados se observó el comportamiento de dos métricas apropiadas para clasificación binaria:
- Exactitud: mide cuantitativamente cuantas predicciones fueron correctas.
- F1: es el promedio ponderado entre la precisión y el *recall*.
- - Precisión: es la habilidad del clasificador de no clasificar una muestra como positiva cuando es negativa.
  - *Recall*: es la capacidad del clasificador de encontrar todas las muestras positivas.

### Resultados de evaluación

| Tipo de modelo | Mejores hiperparámetros | Exactitud (*Accuracy*) | Métrica F1 | 
| --- | --- | --- | --- | 
| Regresión logística | 'C': 0.08011117642517443, 'solver': 'lbfgs' | 0.8448598130841122 | 0.6937269372693727 |
| Bosque aleatorio | 'n_estimators': 73, 'criterion': 'gini', 'max_depth': 50, 'min_samples_split': 20, 'min_samples_leaf': 2, 'min_weight_fraction_leaf': 2.5214105645479093e-05, 'ccp_alpha': 1.8151142421551003e-05, 'max_samples': 0.959999447846922 | 0.8710280373831776 | 0.7544483985765125 |

## Análisis de los resultados

Los resultados del bosque aleatorio mejoran los resultados de la regresión logística, pero se puede mejorar todavía más

## Conclusiones

Se pueden desarrollar otros modelos para mejorar el resultado acá encontrado.

## Referencias

[Bosque aleatrorio en SciKitLearn](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)
