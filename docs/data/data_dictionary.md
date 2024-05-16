# Diccionario de datos

## Base de datos con información tanto clínica como sociodemográfica de pacientes con VIH y sin VIH

<p align="justify">
Para la elaboración del modelo, se emplea la base de datos de Kaggle, que se encuentra en el siguiente enlace: https://www.kaggle.com/datasets/aadarshvelu/aids-virus-infection-prediction/data. El conjunto, de datos contiene información tanto clínica como sociodemográfica de pacientes, donde algunos padecen de VIH y otros no. Por ende, cuenta con los insumos suficientes para la construcción de un modelo de clasificación, que permita predecir si un paciente tiene SIDA (VIH) o no.
</p>

<p align="justify">
El conjunto de datos, contiene una variable dependiente llamada "infected", esta sirve para diferenciar los pacientes que tienen la enfermedad de los que no y hay 22 variables independientes. Además, el conjunto de datos, tiene 2139 observaciones, es decir, pacientes.
</p>

| Variable | Descripción | Tipo de dato | Rango o Valores posibles | Fuente de datos |
| --- | --- | --- | --- | --- |
| time | Tiempo para el fracaso o la censura | int | 14-1231| Kaggle |
| trt | Indicador de tratamiento | int | (0 = solo ZDV; 1 = ZDV + ddI, 2 = ZDV + Zal, 3 = solo ddI) | Kaggle |
| age | Edad del paciente | int | 12-70 | Kaggle|
| wtkg | Masa del paciente en Kilogramos | float | 31-160 | Kaggle |
| hemo | hemofilia |int  | (0=no, 1=si) | Kaggle|
| homo | Actividad homosexual | int | (0=no, 1=si) | Kaggle |
| karnof | Puntuación de Karnofsky | int |(en una escala de 0-100) | Kaggle |
| oprior | Terapia antirretroviral sin ZDV pre-175 | int | (0=no, 1=si) | Kaggle |
| drugs | Antecedentes de uso de drogas intravenosas | int | (0=no, 1=si) | Kaggle |
| z30 | ZDV en los 30 días anteriores al 175 | int | (0=no, 1=si) | Kaggle|
| preanti | días antes de la terapia pre-175 | int | 0-2851 | Kaggle |
| race | Raza | int | (0=blanco, 1=no blanco) | Kaggle|
| gender | Género | int | (0=F, 1=M) | Kaggle |
| str2 | Historia antirretroviral | int | (0=ingenuo, 1=experimentado)  | Kaggle |
| strat | Estratificación de la historia antirretroviral | int | (1='Sin tratamiento antirretroviral',2='> 1 pero <= 52 semanas de terapia antirretroviral previa',3='> 52 semanas) | Kaggle|
| symptom | Indicador sintomático| int | (0=asintomático, 1=sintomático) | Kaggle |
| treat | Tratamiento indicado | int | (0= solo ZDV , 1=otros) | Kaggle|
| offtrt | Indicador de off-trt antes de 96 +/- 5 semanas | int | (0=no,1=si) | Kaggle |
| cd40 | CD4 al inicio | int | 0-1199 | Kaggle |
| cd420 | CD4 a las 20+/-5 semanas | int | 49-1119 | Kaggle|
| cd80 | CD8 al inicio | int | 40-5011 | Kaggle |
| cd820 | CD8 a las 20+/-5 semanas | int | 124-6035 | Kaggle|
| infected | Está infectado con SIDA | int | (0=no, 1=si) | Kaggle |

- **Variable**: nombre de la variable.
- **Descripción**: breve descripción de la variable.
- **Tipo de dato**: tipo de dato que contiene la variable.
- **Rango/Valores posibles**: rango o valores que puede tomar la variable.
- **Fuente de datos**: fuente de los datos de la variable.



