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

La detección temprana del VIH sigue siendo un desafío en muchas áreas, particularmente donde los recursos son limitados. Un diagnóstico temprano es crucial para mejorar los resultados del tratamiento y reducir la transmisión del virus.

Los métodos tradicionales para diagnosticar el VIH pueden ser costosos, invasivos y requerir infraestructura de laboratorio, lo que no siempre está disponible en regiones con recursos limitados. Con base, en lo descrito surge la necesidad de buscar alternativas menos costosas, por esto se plantea la opción de utilizar modelos de machine learning, para realizar el diagnóstico del SIDA (VIH) en pacientes.

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

- Cientifíco de datos junior : Franklin Granadados 
- Cientifíco de datos junior: Julián David Ortiz 
- Cientifíco de datos junior: Juan David Ramírez Ávila 

## Presupuesto

[Descripción del presupuesto asignado al proyecto]

## Stakeholders

- Organizaciones de Salud Pública: Para mejorar las herramientas de diagnóstico y la toma de decisiones clínicas.
- Investigadores y Desarrolladores: Interesados en aplicar técnicas de machine learning en problemas de salud global.
- Comunidades en Regiones de Bajos Recursos: Beneficiándose de herramientas de diagnóstico más accesibles y económicas.

## Aprobaciones

- [Nombre y cargo del aprobador del proyecto]
- [Firma del aprobador]
- [Fecha de aprobación]
