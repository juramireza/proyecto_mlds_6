# Definición de los datos

## Origen de los datos

<p align="justify">
Para la elaboración del modelo, se emplea la base de datos de Kaggle, que se encuentra en el siguiente enlace: https://www.kaggle.com/datasets/aadarshvelu/aids-virus-infection-prediction/data. El conjunto, de datos contiene información tanto clínica como sociodemográfica de pacientes, donde algunos padecen de VIH y otros no. Por ende, cuenta con los insumos suficientes para la construcción de un modelo de clasificación, que permita predecir si un paciente tiene SIDA (VIH) o no.
</p>

<p align="justify">
El conjunto de datos, contiene una variable dependiente llamada "infected", esta sirve para diferenciar los pacientes que tienen la enfermedad de los que no y hay 22 variables independientes. Además, el conjunto de datos, tiene 2139 observaciones, es decir, pacientes.
</p>

<p align="justify">
Los datos fueron extraídos directamente desde la url https://www.kaggle.com/datasets/aadarshvelu/aids-virus-infection-prediction/data?select=AIDS_Classification.csv de Kaggle, para esto tuvo que hacerce una conexión a la API de Kaggle, con el apoyo de una cuenta con acceso a Kaggle y un token.
</p>

## Especificación de los scripts para la carga de datos

<p align="justify">

La carga del conjunto de datos, se hizo utilizando Google Colab para desarrollar el código, Github como repositorio tanto para el código como para el conjunto de datos y dvc, para versionar los datos.

Para la carga de los datos y el versionamiento de estos, se hizo una conexión directa a Kaggle, con los scripts que se listan a continuación:

- https://github.com/juramireza/proyecto_mlds_6/blob/master/scripts/data_acquisition/data_acquisition.py

- https://github.com/juramireza/proyecto_mlds_6/blob/master/scripts/data_acquisition/data_acquisition.ipynb 

</p>

## Referencias a rutas de origen de los datos y destino

- La ruta de origen de los datos, es Kaggle y la url es https://www.kaggle.com/datasets/aadarshvelu/aids-virus-infection-prediction/data?select=AIDS_Classification.csv .

- Las rutas de destino, donde se consolidan los datos, para ser consumidos para el modelamiento son: 

- Con datos atípicos: https://github.com/juramireza/proyecto_mlds_6/blob/master/data/AIDS_cleaned.csv.dvc
- Sin datos atítpicos: https://github.com/juramireza/proyecto_mlds_6/blob/master/data/AIDS_Classification_filtered.csv

### Preprocesamiento del conjunto de datos 

<p align="justify">
El conjunto de datos, contiene una variable dependiente llamada "infected", esta sirve para diferenciar los pacientes que tienen la enfermedad de los que no y hay 22 variables independientes. Además, el conjunto de datos, tiene 2139 observaciones, es decir, pacientes. Y esta en un archivo comprimido .zip y dentro de este, hay un archivo .csv, separado por comas, además el conjunto de datos tiene un formato tabular, es decir, en filas y columnas. 
</p>

<p align="justify">
Se hizo un análisis exploratorio de los datos, y con base en este se detectaron valores atípicos en distintas variables independientes del conjunto de datos, principalmente para las observaciones, que están bajo la categoría de no infectado. Entonces, se hizo una limpieza de datos, retirando aquellas observaciones, que tienen valores atípicos en las variables del conjunto de datos y guardando el conjunto de datos en la ruta, https://github.com/juramireza/proyecto_mlds_6/blob/master/data/AIDS_cleaned.csv.dvc y el original en la ruta, https://github.com/juramireza/proyecto_mlds_6/blob/master/data/AIDS_Classification.csv . También, si hizo un análisis de la distribución de los datos atípicos y como se envidencia en el script https://github.com/juramireza/proyecto_mlds_6/blob/master/scripts/eda/data_analysis.ipynb que la proporción de estos es baja, entonces, para la construcción del modelo, se experimenta realizando el modelo con los datos atípicos y sin los datos atípicos y comparar los resultados obtenidos, dada la baja proporción de outliers, se esperaría que los resultados en ambos casos sean muy similares. 
</p>

<p align="justify">
Adicionalmente, se evidenció que existe un desbalance de clases, entre infectado y no infectado. Ya que, se tiene aproximadamente el triple de observaciones bajo la categoría de no infectado en comparación con la clase de infectado, después de hacer el filtrado de de las observaciones atípicas. Entonces, para hacer el modelammiento, se experimenta construyendo el modelo con el conjunto de datos desbalanceado y luego, sobre el conjunto de datos balanceado, aplicando alguna técnica de balanceo de datos. 

</p>

<p align="justify">
Los scritps, con los que se realizó la limpieza descrita anteriormente, se emplearon los scripts, que se encuentran en las siguientes rutas: 
</p>

- Script con la función de limpieza: https://github.com/juramireza/proyecto_mlds_6/blob/master/scripts/eda/limpieza.py

- Script donde se llama la función de limpieza y se hace un análisis exploratorio preliminar: https://github.com/juramireza/proyecto_mlds_6/blob/master/scripts/data_acquisition/data_acquisition.ipynb


