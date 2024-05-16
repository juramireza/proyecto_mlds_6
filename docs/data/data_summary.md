# Reporte de Datos

Este documento contiene los resultados del análisis exploratorio de datos.

## Resumen general de los datos
<p align="justify">
El conjunto de datos, contiene una variable dependiente llamada "infected", esta sirve para diferenciar los pacientes que tienen la enfermedad de los que no y hay 22 variables independientes. Además, el conjunto de datos, tiene 2139 observaciones, es decir, pacientes.
</p>

<p align="justify">
Entonces, el conjunto de datos tiene 23 variables, en total, que como se aprecia en el diccionario de datos (https://github.com/juramireza/proyecto_mlds_6/blob/master/docs/data/data_dictionary.md) 22 son de tipo entero y una es de tipo float. 
</p>

<p align="justify">
Aunque, las variables trt, hemo, homo, drugs, karnof, oprior, z30, race, gender, str2,strat, symptom, treat, offtrt e infected son variables que realmente hacen refernecia a categorías, es decir, contamos con 15 variables que realmente son categóricas. 
</p>

## Resumen de calidad de los datos


Con base en el análisis realizado se encontró que: 

<p align="justify">
1. Ninguna de las variables tiene valores faltantes.
2. No se tienen observaciones repetidas. 
3. Las variables, no contienen valores faltantes. 
4. Se realizó un gráfico para revisar el número de observaciones por cada categoría en las variables trt, hemo, homo, drugs, karnof, oprior, z30, race, gender, str2,strat, symptom, treat, offtrt e infected. 
</p>

![Texto alternativo](https://github.com/juramireza/proyecto_mlds_6/raw/master/docs/data/CountCategories.png)

<p align="justify">
El gráfico del conteo de observaciones por categoría en cada una de las variables, permite observar que la variable trt que señala un indicador del tratamiento, se tiene cuatro categorías  y que las observaciones están distribuidas de forma relativamente equitativa. En los demás casos, las categorías están desbalanceadas. El caso más llamativo es el de la variable oprior, donde la gran mayoría de las observaciones se encuentran en el valor cero que indica "no": no se cuenta con "Terapia antirretroviral sin ZDV pre-175". Para los otros atributos, es posible apreciar que la mayoría de pacientes:
</p>

* No son hemofílicos.
* Son homosexuales.
* No tienen antecedentes de uso de drogas intravenosas.
* Tienen una puntuación de 100 en la puntuación de Karnofsky.
* Tienen ZDV en los 30 días anteriores al 175.
* Son de "raza" blanca.
* Son de género masculino.
* Son experimentados en su historia antirretroviral.
* No tienen tratamiento antirretroviral. Otro grupo, casi igual, pero un poco menor, han llevado tratamiento por más de 52 semanas.
* Son asintomáticos.
* El tratamiento indicado está en "otros" (no es solo ZDV).
* No tiene indicador de off-trt antes de 96 +/- 5 semanas.
* No está infectado con SIDA.

## Variable objetivo

<p align="justify">
También es importante analizar la variable infected, ya que, es la variable dependiente, es decir, la variable objetivo y que se desea predecir. Ya que, se desea construir un modelo capaz de predicir si un paciente tiene VIH (SIDA) o no. 
</p>

<p align="justify">
A continuación, se presenta un gráfico que permite apreciar la distribución de la variable infected, y se observa que, estamos frente a un conjunto de datos desbalanceado, ya que, aproximadamente el 25 % de los pacientes están infectados y el otro 75 %, no lo esta. Entonces, para cuando se vaya a realizar el modelo, se deben aplicar técnicas de balanceo o realizar un muestreo, con el fin de obtener un conjunto de datos balanceado, dado que el conjunto de datos es relativamente pequeño 2139 observaciones, es viable inclinarse, por la opción de aplicar una técnica para balancear el conjunto de datos, es decir, para igual el número de observaciones de pacientes infectados y no infectados. 
</p>

![Texto alternativo](https://github.com/juramireza/proyecto_mlds_6/raw/master/docs/data/Distribution_Infected.png)


## Variables individuales

<p align="justify">
Posteriormente, se analizó la distribución de las 15 variables categóricas en función de la variable objetivo (infected) como se muestra en el gráfico a continuación, en este, se aprecia que variables como oprior y homo, tienen la mayoría de las observaciones, en una sola categoría, principalmente la variable oprior, donde el 97.8 % de las observaciones del conjunto de datos, estan en la categoría de cero, por ende, esta sería una variable candidata a eliminar para hacer el modelamiento. 
</p>

![Texto alternativo](https://github.com/juramireza/proyecto_mlds_6/raw/master/docs/data/Distribution_infected_categorical.png)

A continuación, se presenta un gráfico en el que se aprecia un histograma para cada una de las variables numéricas, en este se aprecia que variables como "age" y "wtkg", tienden a tener una distribución normal, 

![Texto alternativo](https://github.com/juramireza/proyecto_mlds_6/raw/master/docs/data/HistNumericalVariables.png)

Para las otras variables es difícil inferir el tipo de distribución, por ende, se hizo un análisis de cada una apoyándose en estadísticos descriptivos numéricos, obteniendo que los individuos del estudio en promedio o media: 

* Tienen un tiempo  879 días para el fracaso o la sensura.
* Tienen una edad de 35 años.
* Tienen un peso de 75 kilogramos.
* Tienen 379 días en la terapia anti-retroviral pre-175.
* Tienen un valor base de 350 en cd4.
* Tienen un valor de 371 en cd4 a las 20 semanas (subió en promedio).
* Tienen un valor base de 986 en cd8.
* Tienen un valor de 938 en cd8 a las 20 semanas (bajó en promedio).

Y en la imágen que se observa, seguidamente se validan los datos mencionados anteriormente, y adicionalmente, para cada una de las variables, se aprecian estadísticos descriptivos, como la desviación estándar, el minímo, el máximo y los cuartiles (25, 50 y 75). 

![Texto alternativo](https://github.com/juramireza/proyecto_mlds_6/raw/master/docs/data/NumericalStatisticians.PNG)

<p align="justify">
Posteriormente, se realizó un gráfico en el que se muestran los histogramas de cada variables numérica, diferenciando por la variable "infected", es decir, la variable objetivo. Y también se construyeron, diagramas de caja y bigotes, para revisar los datos atípicos en cada una de las variables y diferenciando por cada clase. Consecutivamente, se presentan estos dos gráficos. 
</p>

![Texto alternativo](https://github.com/juramireza/proyecto_mlds_6/raw/master/docs/data/HistInfected.png)

<p align="justify">
En el gráfico de los histogramas de cada variable, diferenciando por la variable objetivo infected, se aprecia que las distribuciones al observarse por clase, no son similares. 
</p>

![Texto alternativo](https://github.com/juramireza/proyecto_mlds_6/raw/master/docs/data/BoxPlotInfected.png)

<p align="justify">
Y al analizar, los Boxplot de cada variable, diferenciados por la variable objetivo, se identifica la presencia de valores atípicos. Entonces, se procede a revisar, el número de valores atípicos en cada variable y calcular la proporción de estos con base en el total de observaciones y se obtienen los resultados de la tabla que se muestra seguidamente:
</p>

![Texto alternativo](https://github.com/juramireza/proyecto_mlds_6/raw/master/docs/data/Atipicos.PNG)

<p align="justify">
Entonces, se evidencia que la propoción de valores atípicos, con base en el total es baja, por ende, es viable dejarlos para el modelamiento. Entonces, se planea experimentar durante el modelamiento, con un conjunto de datos, con los valores atípicos y sin los valores atípicos. 
</p>

## Relación entre variables explicativas 

<p align="justify">
Después,  se hizo un análisis de correlación entre las variables numéricas y se construyó el gráfico de correlación que se aprecia a continuación: 

![Texto alternativo](https://github.com/juramireza/proyecto_mlds_6/raw/master/docs/data/CorrNum.png)

Fuera de la diagonal, las correlaciones más altas las encuentro entre las variables "cd40" con "cd420" y "cd80" con "cd820". Como representan la misma medición de un parámetro en diferentes momentos, se propone para ambos casos calcular una variable que sea la diferencia, por ejemplo cd420-cd40 y quitar las dos varibles originales, con el fin de evitar problemas de multicolinealidad. 

Después, se hace un diagrama de correlación, con todas las variables del conjunto de datos, como se observa inmediatamente: 

![Texto alternativo](https://github.com/juramireza/proyecto_mlds_6/raw/master/docs/data/CorrTotal.png)

Con base en el gráfico de correlación, se aprecia que existen variables altamente correlacionadas y con base en ello se proponen las siguientes estrategias: 

* Entre "treat" y "trt", conservar "trt", que posee más información respecto a la otra.

* Entre "strat", "srt2", "z30" y "preanti", conservar "preanti", que es una variable numérica con mayor información que las categóricas.

* Entre "gender" y "homo", conservar solo la variable "gender". La variable "homo" ya mostraba sesgo. 

</p>

## Ranking de variables

Después de aplicar las estrategias, mencionadas en el apartado anterior, se procedió nuevamente a realizar el gráfico de correlación y se obtuvieron los siguientes resultados:

![Texto alternativo](https://github.com/juramireza/proyecto_mlds_6/raw/master/docs/data/CorrFinal.png)

Y con base, en el diagrama final de correlación se construye la siguiente tabla, en la que se aprecia un ranking de importancia de las variables independientes para predecir la variable dependiente infected, con base en le valor absoluto de la correlación de esta, con las otras variables. 

| Variable | Valor absoluto de la correlación con infected | Ranking | 
| --- | --- | --- | 
| time | 0.57 | 1 |
| dif_cd4 | 0.23 | 2 | 
| preanti | 0.13| 3 | 
| symptom | 0.13 | 4 | 
| treat | 0.13 | 5 | 
| karnof | 0.1 | 6 | 
| offtrt | 0.09 | 7 | 
| age | 0.07 | 8 | 
| dif_cd8 |0.07 | 9| 
| race | 0.06 | 10 | 
| drugs | 0.05 | 11 | 
| gender | 0.05 | 12 | 
| wtkg | 0.02 | 13 | 
| hemo |0.01  | 14| 

El análisis expuesto, se encuentra con mayor detalle en el script: https://github.com/juramireza/proyecto_mlds_6/blob/master/scripts/eda/data_analysis.ipynb

