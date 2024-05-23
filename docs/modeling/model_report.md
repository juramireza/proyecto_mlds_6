# Reporte del Modelo Final

## Resumen Ejecutivo

<p align="justify">
En esta sección se presenta un resumen de los resultados obtenidos con el mejor modelo, que fue el que su obtuvo de la aplicación del algoritmo de bosques aleatorios (Random forest). 
</p>

<p align="justify">

El clasificador de bosques aleatorios consiste en una colección de árboles de decisión entrenados en muestras distintas que realizan una "votación" para elegir la clasificación más favorable. La cantidad de árboles que se entrenan se define con el hiperparámetro "n_estimators", y se pueden configurar los hiperparámetros de estos árboles, como por ejemplo la cantidad máxima de características a considerar con "max_features". (Tomado del material de estudio de módulo 2).

</p>

## Descripción del Problema

<p align="justify">
La detección temprana del VIH sigue siendo un desafío en muchas áreas, particularmente donde los recursos son limitados. Un diagnóstico temprano es crucial para mejorar los resultados del tratamiento y reducir la transmisión del virus.
</p>

<p align="justify">
Los métodos tradicionales para diagnosticar el VIH pueden ser costosos, invasivos y requerir infraestructura de laboratorio, lo que no siempre está disponible en regiones con recursos limitados. Con base, en lo descrito surge la necesidad de buscar alternativas menos costosas, por esto se plantea la opción de utilizar modelos de machine learning, para realizar el diagnóstico del SIDA (VIH) en pacientes.
</p>

<p align="justify">
Entonces, con este proyecto se buscaba construir un modelo, que basándose tanto en información clínica como socio demográfica, permita predecir si un paciente tiene el virus del VIH (SIDA o no). Entonces, como la cuestión a resolver consiste en determinar si un paciente pertenece a la categoría de los que tienen VIH (SIDA) o no pertenece a esta clase, entonces, el problema a resolver, era de clasificación binaria, por ende, los esfuerzos se centraron en construir un modelo de clasificación utilizando distintos algoritmos como la regresión logística, los bosques aleatorios, las máquinas de soporte vectorial o el el algoritmo de los vecinos más cercanos. 
</p>

## Descripción del Modelo

<p align="justify">
Se construyó un modelo de clasificación binaria y para su elaboración se siguieron los siguientes pasos: 
</p>

<p align="justify">
1. Se realizó un análisis exploratorio de los datos, para determinar que variables eran importantes para el modelo y con base en este, se hizo la extracción de características, es decir, se le dio tratamiento a las variables según su tipo, antes de ser ingresadas al modelo. 
</p>

<p align="justify">
2. Se identificó, que el conjunto de datos, estaba desbalanceado, por ende, se aplico la técnica SMOTE, con el fin de obtener un conjunto de datos, donde el número de observaciones para ambas clases, estuviese equitativamente distribuido. 
</p>

<p align="justify">
4. Se realizaron varios experimentos, combinando tanto distintos algoritmos, como varias configuraciones de hiperparámetros haciendo uso de herramientas como mlflow y optuna.
</p>

<p align="justify">
5. Por último, se evaluaron los modelos, con base en la matriz de confusión y las métricas de exactitud y F1-Score. 
</p>

## Evaluación del Modelo

A continuación, se presenta la matriz de confusión del mejor modelo obtenido, que fue el que se logró, con el algoritmo de bosques aleatorios:

![Texto alternativo](https://github.com/juramireza/proyecto_mlds_6/blob/master/mlruns/svm_/5d5755ad623048c192007bad0d5fe420/artifacts/confusion_matrix/confusion_matrix.png)

## Conclusiones 

<p align="justify">

- Con el algoritmo de bosques aleatorios, se consiguen los mejores resultados. Ya que, con este se consiguen los valores más altos tanto de Exactitud (0.87) como de F1 Score (0.75), después se tiene el modelo construido con el algoritmo de SVM, con una Exactitud de 0.86 y un F1 Score de 0.72, luego esta el modelo elaborado con el algoritmo de regresión logística con una Exactitud de 0.84 y un F1 Score de 0.69. Y por último, siendo el modelo con peores métricas, se encuentra el que se desarrollo con el algoritmo de k-NN, con una Exactitud de 0.83 y un F1 Score de 0.67. 
</p>

<p align="justify">

- Es viable utilizar el modelo construído, como un sistema de priorización, es decir, las entidades cuidadoras de salud, pueden estar corriendo este modelo, sobre los pacientes de los que tengan la información clínica y sociodemográfica, con el fin de que si alguien reporta una alta probabilidad de tener el virus del SIDA (VIH), se le hagan otros estudios con prontitud, para validar si efectivamente tienen la enferemdad o no. En conclusión, es viable usar el modelo con una herramienta de priorización y salud preventiva, más no puede ser empleada como una herramienta que diagnóstique la enfermadad y sea la última palabra. 

</p>

## Recomendaciones
A continuación, se presentan algunas sugerencias, con el fin de construir un modelo que consiga mejores resultados: 

- Experimentar con algoritmos diferentes a los utilizados en este proyecto
- Revisar aquellas observaciones que están siendo mal clasificadas e intentar comprender esto porque sucede. 
- Iterar en el proceso completo, es decir revisar el análisis exploratorio y ver que variables valdría la pena incluir y que variables, es mejor excluir. 
- En caso de ser viable, conseguir más observaciones con el fin de aumentar el conjunto de datos. 
- Si existe la posibilidad, explorar nuevas variables. 

## Referencias

[Bosque aleatrorio en SciKitLearn](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)

