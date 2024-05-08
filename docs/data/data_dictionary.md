# Diccionario de datos

## Base de datos con información tanto clínica como sociodemográfica de pacientes con VIH y sin VIH

<p align="justify">
Para la elaboración del modelo, se emplea la base de datos de Kaggle, que se encuentra en el siguiente enlace: https://www.kaggle.com/datasets/aadarshvelu/aids-virus-infection-prediction/data. El conjunto, de datos contiene información tanto clínica como sociodemográfica de pacientes, donde algunos padecen de VIH y otros no. Por ende, cuenta con los insumos suficientes para la construcción de un modelo de clasificación, que permita predecir si un paciente tiene SIDA (VIH) o no.

El conjunto de datos, contiene una variable dependiente llamada "infected", esta sirve para diferenciar los pacientes que tienen la enfermedad de los que no y hay 22 variables independientes. Además, el conjunto de datos, tiene 2139 observaciones, es decir, pacientes.
</p>

| Variable | Descripción | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| --- | --- | --- | --- | --- |
| time | Tiempo para el fracaso o la censura | int | 14-1231| Kaggle |
| trt | Indicador de tratamiento | int | (0 = solo ZDV; 1 = ZDV + ddI, 2 = ZDV + Zal, 3 = solo ddI) | Kaggle |
| age | Edad del paciente | int | 12-70 | Kaggle|
| wtkg | Masa del paciente en Kilogramos | float | 31-160 | Kaggle |
| hemo | hemofilia |int  | Rango/Valores posibles | Kaggle|
| homo | Actividad homosexual | int | Rango/Valores posibles | Kaggle |
| karnof | Puntuación de Karnofsky | int | Rango/Valores posibles | Kaggle |
| oprior | Terapia antirretroviral sin ZDV pre-175 | int | Rango/Valores posibles | Kaggle |
| drugs | Antecedentes de uso de drogas intravenosas | int | Rango/Valores posibles | Kaggle |
| z30 | ZDV en los 30 días anteriores al 175 | int | Rango/Valores posibles | Kaggle|
| preanti | días antes de la terapia pre-175 | int | Rango/Valores posibles | Kaggle |
| race | Carrera | int | Rango/Valores posibles | Kaggle|
| gender | Género | int | Rango/Valores posibles | Kaggle |
| str2 | Historia antirretroviral | int | Rango/Valores posibles | Kaggle |
| strat | Estratificación de la historia antirretroviral | int | Rango/Valores posibles | Kaggle|
| symptom | Indicador sintomático| int | Rango/Valores posibles | Kaggle |
| treat | Tratamiento indicado | int | Rango/Valores posibles | Kaggle|
| offtrt | Indicador de off-trt antes de 96 +/- 5 semanas | int | Rango/Valores posibles | Kaggle |
| cd40 | CD4 al inicio | int | Rango/Valores posibles | Kaggle |
| cd420 | CD4 a las 20+/-5 semanas | int | Rango/Valores posibles | Kaggle|
| cd80 | CD8 al inicio | int | Rango/Valores posibles | Kaggle |
| cd820 | CD8 a las 20+/-5 semanas | int | Rango/Valores posibles | Kaggle|
| infected | Está infectado con SIDA | int | Rango/Valores posibles | Kaggle |



- **Variable**: nombre de la variable.
- **Descripción**: breve descripción de la variable.
- **Tipo de dato**: tipo de dato que contiene la variable.
- **Rango/Valores posibles**: rango o valores que puede tomar la variable.
- **Fuente de datos**: fuente de los datos de la variable.



