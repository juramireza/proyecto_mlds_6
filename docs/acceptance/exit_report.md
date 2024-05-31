# Informe de salida

## Resumen Ejecutivo

<p align="justify">

Este informe describe los resultados obtenidos con el proyecto "Modelo de predictivo basado en aprendizaje de máquina para la detección del SIDA (VIH) con base en información clínica y sociodemográfica" y presenta tanto los principales logros como las lecciones aprendidas durante el proceso.

</p>


### Resultados del proyecto

#### 1. Resumen de los entregables y logros alcanzados en cada etapa del proyecto:

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

<p align="justify">

- Deployment: En esta última sección, se realizó el despliegue del modelo construído con el algoritmo de bosques aleatorios, utilizando la herramienta de mlfow. 

</p>

<p align="justify">

- Evaluación del modelo final: En esta sección, se muestra una comparación de todos los modelos construídos y se observa, que los mejores resultados, se obtuvieron empleando el algoritmo de bosques aleatorios. 

</p>



<p align="justify">
En los modelos empleados se observó principalmente el comportamiento de dos métricas apropiadas para clasificación binaria, la exactitud y el F1 score. A continuación, se presenta una descripción de las métricas mencionadas y adicionalmente tanto del Recall como de la Precisión. 

</p>

* *Exactitud*: mide cuantitativamente cuantas predicciones fueron correctas.
*  *Recall*: Proporción de verdaderos positivos entre los positivos reales.
* *Precisión*: es la habilidad del clasificador de no clasificar una muestra como positiva cuando es negativa.
* *F1 score*: El F1 score es la media armónica de la precisión y el recall. Un F1 score alto indica un buen equilibrio entre precisión y exhaustividad.

#### Resultados de evaluación

| Tipo de algoritmo | Mejores hiperparámetros | Exactitud (*Accuracy*) | F1 Score| 
| --- | --- | --- | --- | 
| Regresión logística | 'C': 0.08011117642517443, 'solver': 'lbfgs' | 0.8448598130841122 | 0.6937269372693727 |
| Bosques aleatorios | 'n_estimators': 73, 'criterion': 'gini', 'max_depth': 50, 'min_samples_split': 20, 'min_samples_leaf': 2, 'min_weight_fraction_leaf': 2.5214105645479093e-05, 'ccp_alpha': 1.8151142421551003e-05, 'max_samples': 0.959999447846922 | 0.8710280373831776 | 0.7544483985765125 |
| SVM | 'C': 2.7807647750443065,'break_ties': False,'cache_size': 200,'class_weight': None,'coef0': 0.0,'decision_function_shape': 'ovr','degree': 3,'gamma': 'scale','kernel': 'rbf', 'max_iter': -1, 'probability': False,'random_state': None,'shrinking': True, 'tol': 0.001,'verbose': False |  0.8635514018691589 | 0.7224334600760456 |
| k-NN |'algorithm': 'auto','leaf_size': 80,'metric': 'minkowski','metric_params': None 'n_jobs': None,'n_neighbors': 20,'p': 1,'weights': 'uniform'| 0.8317757009345794 | 0.6785714285714285 |
| ANN | 'n_layers': 1, 'n_nodes': 86, 'dp': 0.3048343482717873, 'activation': 'relu6', 'learning_rate': 0.00018564900166494438 | 0.8766355 | 0.7421875 |
| GBM | 'subsample': 0.7,  'n_estimators': 100,  'min_samples_split': 5,  'min_samples_leaf': 5,  'max_depth': 6,  'learning_rate': 0.1 | 0.88| 0.71 |
|DT | 'splitter': 'random',  'min_samples_split': 2,  'min_samples_leaf': 20,  'max_features': None,  'max_depth': 9,  'criterion': 'gini | 0.87| 0.69 |

#### Análisis de los resultados

<p align="justify">
Con el algoritmo de bosques aleatorios, se consiguen los mejores resultados. Ya que, con este se consiguen los valores más altos tanto de Exactitud (0.87) como de F1 Score (0.75). Esto, significa que es el modelo, que más observaciones ha conseguido clasificar correctamente y el que logra un mejor balance entre precisión y exhaustividad.
</p>

<p align="justify">
El algoritmo de máquinas de soporte vectorial, arroja resultados inferiores que el de Bosques Alatorios, con una Exactitud de 0.86 y un F1 Score de 0.72. Pero, con estas métricas tiene mejor desempeño, que los modelos obtenidos con los algoritmos de k-NN y Regresión logística. 
</p>

<p align="justify">
El modelo construído con el algoritmo de regresión logística registro una Exactitud de 0.84 y un F1 Score de 0.69, métricas inferiores a las obtenidas tanto con Bosques aleatorios como con SVM, pero superiores a las que se lograron al aplicar el algoritmo de k-NN. Es decir, el modelo con las peores métricas fue este, con una Exactitud de 0.83 y un F1 Score de 0.67.
</p>

<p align="justify">
Con Arboles de descision se alcanzo un Accuracy de 0.87% coon un F1 score de 0.69. Aunque el modelo tiene una alta exactitud, su F1 de indica que tiene problemas para equilibrar la precisión y la exhaustividad, sugiriendo posibles desbalances en las clases o problemas con falsos positivos/negativos. Es posible ajustar el umbral de decisión y considerar técnicas para balancear las clases, como el submuestreo, sobremuestreo o el uso de SMOTE.
</p>

<p align="justify">
Aunque el modelo GBM tiene una alta exactitud de 0.88, la puntuación F1 de 0.71 indica que podría estar enfrentando problemas de equilibrio entre precisión y exhaustividad, probablemente debido a un desbalance de clases o errores en falsos positivos/negativos. Para mejorar el rendimiento, se recomienda ajustar el umbral de decisión y aplicar técnicas de balanceo de clases, como submuestreo, sobremuestreo o el uso de SMOTE, para asegurar que el modelo maneje de manera más efectiva ambas clases.
</p>

<p align="justify">
La búsqueda de hiperparámetros utilizando Randomized Search mejoró significativamente el rendimiento de los modelos, elevando la exactitud a 0.88 y la puntuación F1 a 0.71 al GBM. Esto demuestra que ajustar adecuadamente los hiperparámetros puede equilibrar mejor la precisión y la exhaustividad, optimizando la capacidad del modelo para manejar el desbalance de clases y reducir errores en falsos positivos y negativos.
</p>

<p align="justify">
Con la red neuronal artificial desarrollada da resultados muy parecidos al modelo de bosque aleatorio. La exactitud es ligeramente superior, por 5 milésimas, pero la métrica F1 es una centésima inferior. En comparación de la red neuronal y el bosque aleatorio desde la matriz de confusión, a la red neuronal le va mejor prediciendo no infectados (374 contra 360), pero le va peor prediciendo infectados (95 contra 106). Eso explica la pequeña diferencia en las métricas
</p>

<p align="justify">
Adicionalmente, se presenta la matriz de confusión del mejor modelo obtenido, que fue el que se logró, con el algoritmo de bosques aleatorios:
</p>

![Texto alternativo](https://github.com/juramireza/proyecto_mlds_6/blob/master/mlruns/ran_for/2a6b1b0fa28c4285a52932f421cdd351/artifacts/confusion_matrix/confusion_matrix.png)

De la matriz de consfusión es importante tener en cuenta lo siguiente: 

- VP : Verdaderos positivos, es decir, son los pacientes que tienen VIH y el modelo predijo correctamente que poseen el virus. Con base en la matriz de confusión se obtuvo un valor 106 pacientes. 

- VN : Verdaderos negativos, es decir, son pacientes que no tienen VIH y le modelo predijo correctamente que no tienen el virus. Con base en la matriz de confusión se obtuvo un valor de 360 pacientes. 

- FP: Falsos positivos, es decir, son pacientes que no tienen el virus, pero el modelo dice que si lo tienen. Con base en la matriz de confusión se obtuvo un valor de 51 pacientes. 

- FN: Falsos negativos, es decir, son pacientes que tienen el virus, pero el modelo predijo que no lo tienen. Con base en la matriz de confusión se obtuvo un valor de 18 pacientes. 

Con base en la matriz de confusión, se calculan las siguientes métricas:

<p align="justify">

- Exactitud (Accuracy): Indica la cantidad de observaciones que fueron clasificadas correctamente por el modelo. Para esta métrica se obtuvo un valor de 0.86, ya que, 462 observaciones se clasificaron bien en relación con un total de 535, que fue el conjunto de pacientes utilizado para la realizar las pruebas sobre el modelo, en datos con los que no había sido entrenado. 

</p>

<p align="justify">

- Precisión (Precision): Para esta métrica, se obtiene un valor de 0.68, lo que es un valor no tan satisfactorio, esta métrica es la división entre los VP y la suma de los VP con los FP. Entonces, la métrica baja porque se tiene un valor alto de FP (51). Entonces, el modelo esta clasificando bastantes pacientes, que no tienen el virus como si lo tuvieran. 

</p>

<p align="justify">

- Sensibilidad (Recall): Para esta métrica, se obtiene un valor de 0.85, lo que es un valor bastante bueno, esta métrica es el cociente entre los VP y la suma de los VP con los FN. Entonces, la métrica es alta porque se tiene un valor bajo de FN (18). Es decir, solamente hay 18 pacientes, que realmente tienen el virus del VIH y el modelo predijo, que eran pacientes sanos. 

</p>

<p align="justify">

- F1-Score: es una métrica, que sirve para evaluar precisión y sensibilidad juntas. Y se obtuvo un valor de 0.75.
</p>

<p align="justify">
Para evaluar los modelos, se utilizó el F1-Score, con el fin de buscar el modelo que mejor equilibrio logrará entre precisión y sensibilidad, siendo el modelo elaborado con bosques aleatorios y con un F1-Score de 0.75.

</p>

<p align="justify">
Aunque es bueno mencionar, que dependiendo del contexto y la necesidad, sería viable inclinarse por otra métrica, por ejemplo, para este caso, es posible que al hablar con personas de negocio, ellos comenten, que para ellos tener bajos valores de presicion, es decir que el modelo calsifique pacientes, que no tienen el virus como si lo tuvieran, no es grave para el proceso. Que lo crítico es que el modelo clasifique pacientes que tienen el virus, en la categoría de que no lo tienen. Por ende, bajo esta premisa la métrica para
evaluar los modelos debe ser la sensibilidad, aunque se pierda presicion. 
</p>




## Conclusiones


<p align="justify">

- Con el algoritmo de bosques aleatorios, se consiguen los mejores resultados. Ya que, con este se consiguen los valores más altos tanto de Exactitud (0.87) como de F1 Score (0.75), después se tiene el modelo construido con el algoritmo de SVM, con una Exactitud de 0.86 y un F1 Score de 0.72, luego esta el modelo elaborado con el algoritmo de regresión logística con una Exactitud de 0.84 y un F1 Score de 0.69. Y por último, siendo el modelo con peores métricas, se encuentra el que se desarrollo con el algoritmo de k-NN, con una Exactitud de 0.83 y un F1 Score de 0.67. 

</p>


<p align="justify">

- Como producto final, se desplegó el modelo construído con el algoritmo de bosques aleatorios en el API de MLflow, para que sea consumido por distintos usuarios. Y predecir, si un paciente padece de VIH (SIDA) o no. 

</p>


## Recomendaciones
A continuación, se presentan algunas sugerencias, con el fin de construir un modelo que consiga mejores resultados: 

- Experimentar con algoritmos diferentes a los utilizados en este proyecto
- Revisar aquellas observaciones que están siendo mal clasificadas e intentar comprender esto porque sucede. 
- Iterar en el proceso completo, es decir revisar el análisis exploratorio y ver que variables valdría la pena incluir y que variables, es mejor excluir. 
- En caso de ser viable, conseguir más observaciones con el fin de aumentar el conjunto de datos. 
- Si existe la posibilidad, explorar nuevas variables. 

## Lecciones aprendidas

<p align="justify">
- El conjunto de datos, estaba desbalanceado, ya que, se tenían mayor cantidad de observaciones de personas sanas, que de personas enfermas. Entonces, esto es posible que sesgue el modelamiento, entonces, se tuvo que aplicar técnicas de balanceo de datos. 
</p>

<p align="justify">
- El aplicar algoritmos de optimización como optuna, permite determinar con precisión y velocidad, los hiperparámetros, con los que se consigue el mejor modelo. 
</p>

## Impacto del proyecto

<p align="justify">

Es viable utilizar el modelo construído, como un sistema de priorización, es decir, las entidades cuidadoras de salud, pueden estar corriendo este modelo, sobre los pacientes de los que tengan la información clínica y sociodemográfica, con el fin de que si alguien reporta una alta probabilidad de tener el virus del SIDA (VIH), se le hagan otros estudios con prontitud, para validar si efectivamente tienen la enfermedad o no. En conclusión, es viable usar el modelo con una herramienta de priorización y salud preventiva, más no puede ser empleada como una herramienta que diagnóstique la enfermadad y sea la última palabra.

</p>

## Agradecimientos

- Agradecimientos al equipo del diplomado en ciencia de datos y machine learning avanzado de la Universidad Nacional de Colombia. 
