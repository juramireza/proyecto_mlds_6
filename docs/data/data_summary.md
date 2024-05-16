# Reporte de Datos

Este documento contiene los resultados del análisis exploratorio de datos.

## Resumen general de los datos
<p align="justify">
El conjunto de datos, contiene una variable dependiente llamada "infected", esta sirve para diferenciar los pacientes que tienen la enfermedad de los que no y hay 22 variables independientes. Además, el conjunto de datos, tiene 2139 observaciones, es decir, pacientes.

Entonces, el conjunto de datos tiene 23 variables, en total, que como se aprecia en el diccionario de datos (https://github.com/juramireza/proyecto_mlds_6/blob/master/docs/data/data_dictionary.md) 22 son de tipo entero y una es de tipo float. 

Aunque, las variables trt, hemo, homo, drugs, karnof, oprior, z30, race, gender, str2,strat, symptom, treat, offtrt e infected son variables que realmente hacen refernecia a categorías, es decir, contamos con 15 variables que realmente son categóricas. 

</p>

## Resumen de calidad de los datos
<p align="justify">

Con base en el análisis realizado se encontró que: 

1. Ninguna de las variables tiene valores faltantes.
2. No se tienen observaciones repetidas. 
3. Se realizó un gráfico para revisar el número de observaciones por cada categoría en las variables trt, hemo, homo, drugs, karnof, oprior, z30, race, gender, str2,strat, symptom, treat, offtrt e infected. 

![test](docs/data/CountCategories.png)


En esta sección se presenta un resumen de la calidad de los datos. Se describe la cantidad y porcentaje de valores faltantes, valores extremos, errores y duplicados. También se muestran las acciones tomadas para abordar estos problemas.

</p>
## Variable objetivo

En esta sección se describe la variable objetivo. Se muestra la distribución de la variable y se presentan gráficos que permiten entender mejor su comportamiento.

## Variables individuales

En esta sección se presenta un análisis detallado de cada variable individual. Se muestran estadísticas descriptivas, gráficos de distribución y de relación con la variable objetivo (si aplica). Además, se describen posibles transformaciones que se pueden aplicar a la variable.

## Ranking de variables

En esta sección se presenta un ranking de las variables más importantes para predecir la variable objetivo. Se utilizan técnicas como la correlación, el análisis de componentes principales (PCA) o la importancia de las variables en un modelo de aprendizaje automático.

## Relación entre variables explicativas y variable objetivo

En esta sección se presenta un análisis de la relación entre las variables explicativas y la variable objetivo. Se utilizan gráficos como la matriz de correlación y el diagrama de dispersión para entender mejor la relación entre las variables. Además, se pueden utilizar técnicas como la regresión lineal para modelar la relación entre las variables.
