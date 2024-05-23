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

En esta sección se describirá el modelo final que se desarrolló para resolver el problema planteado. Se debe incluir una descripción detallada del modelo, la metodología utilizada y las técnicas empleadas.

## Evaluación del Modelo

En esta sección se presentará una evaluación detallada del modelo final. Se deben incluir las métricas de evaluación que se utilizaron y una interpretación detallada de los resultados.

## Conclusiones y Recomendaciones

En esta sección se presentarán las conclusiones y recomendaciones a partir de los resultados obtenidos. Se deben incluir los puntos fuertes y débiles del modelo, las limitaciones y los posibles escenarios de aplicación.

## Referencias

[Bosque aleatrorio en SciKitLearn](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)

