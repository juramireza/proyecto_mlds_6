# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

"Modelo de predictivo para la detección del SIDA (VIH) con base en información clínica y sociodemográfica”

## Objetivo del Proyecto a construir

Desarrollo y Evaluación de Modelos de Aprendizaje Automático para la Detección del Virus de la Inmunodeficiencia Humana (VIH) mediante Datos Clínicos: Mejorando la Detección Temprana y la Gestión del Tratamiento.

### Objetivos específicos

1.Realizar una selección adecuada de las variables con base en un análisis exploratorio de la base de datos clínicos. 

2.Implementar tanto estrategias de control de versiones de código como de datos.

3.Construir modelos de machine lerning para la detección de VIH aplicando distintos algoritmos de la ciencia de datos y/o la inteligencia artificial. 

4.Utilizar MLflow para el seguimiento de experimentos, gestión de modelos y almacenamiento de artefactos.

5.Construcción de una API para acceder y consumir el modelo de detección del VIH construído. 


## Alcance del Proyecto a construir

El proyecto se desarrolla en un período de 5 semanas, utilizando una base de datos clínicos y se centra en la construcción y despliegue de una herramienta, que permita la detección del virus del SIDA (VIH) con base en variables clínicas y sociodemográficas.  

Para la elaboración del modelo, se emplea la base de datos de Kaggle, que se encuentra en el siguiente enlace: https://www.kaggle.com/datasets/aadarshvelu/aids-virus-infection-prediction/data. El conjunto, de datos contiene información tanto clínica como sociodemográfica de pacientes, donde algunos padecen de VIH y otros no. Por ende, se cuenta con los insumos suficientes para la construcción de un modelo de clasificación, que permita predecir si un paciente tiene SIDA (VIH) o no. El conjunto de datos, contiene una variable dependiente llamada "infected", esta sirve para diferenciar los pacientes que tienen la enfermedad de los que no y hay 22 variables independientes, que es viable utilizar para realizar la predicción. Además, el conjunto de datos, tiene 2139 observaciones, es decir, pacientes. 

Al finalizar el proyecto, se desea un modelo que consiga predecir si un paciente tiene SIDA (VIH) o no, con el menor grado de incertidumbre y que este desplegado, de tal forma, que pueda ser consumido por un usuario final. 

## Metodología

[Descripción breve de la metodología que se utilizará para llevar a cabo el proyecto]

## Cronograma

| Etapa | Duración Estimada | Fechas |
|------|---------|-------|
| Entendimiento del negocio y carga de datos | 1 semana | del 6 de mayo al 10 de mayo |
| Preprocesamiento, análisis exploratorio | 1 semana | del 13 de mayo al 17 de mayo |
| Modelamiento y extracción de características | 1 semana | del 20 de mayo al 24 de mayo |
| Despliegue | 1 semana | del 27 de mayo al 31 de mayo |
| Evaluación y entrega final | 1 semana | del 3 de junio al 7 de junio |



## Equipo del Proyecto

- [Nombre y cargo del líder del proyecto]
- [Nombre y cargo de los miembros del equipo]

## Presupuesto

[Descripción del presupuesto asignado al proyecto]

## Stakeholders

- [Nombre y cargo de los stakeholders del proyecto]
- [Descripción de la relación con los stakeholders]
- [Expectativas de los stakeholders]

## Aprobaciones

- [Nombre y cargo del aprobador del proyecto]
- [Firma del aprobador]
- [Fecha de aprobación]
