# Despliegue de modelos

## Infraestructura

- **Nombre del modelo:** final_model 
- **Plataforma de despliegue:** El despliegue se hizo utilizando la herramienta de mlflow
- **Requisitos técnicos:** Se  requieren las siguientes herramientas, que se encuentran en los enlaces que se presentan a continuación: 
   

    * Entorno de python: https://github.com/juramireza/proyecto_mlds_6/blob/master/mlruns/final_model/f07e5539accd45dea6c796a24f65dd04/artifacts/final_model/python_env.yaml
   

  
    * Bibliotecas: https://github.com/juramireza/proyecto_mlds_6/blob/master/mlruns/final_model/f07e5539accd45dea6c796a24f65dd04/artifacts/final_model/requirements.txt. Para mayor detallar de los requerimientos con relación al entorno de python y las bibliotecas necesarias para realizar el despliegue del modelo, es viable consultarlos en  https://github.com/juramireza/proyecto_mlds_6/tree/master/mlruns/final_model/f07e5539accd45dea6c796a24f65dd04/artifacts/final_model  
 
    
   <p align="justify">
    * Software: Se requiere una herramienta para desarrollar en python y sea viable instalar la biblioteca de mlflow. Para este proyecto se empleo el ambiente de google colab, en el que se instaló la librería de mlflow y en conjunto, con la interfaz de mlflow, se hizo el despliegue del modelo. Hay que recordar, que como se empleo Google Colab, para realizar el despliegue del modelo, entonces, también se hizo uso de la herramienta pyngrok, con el objetivo de conectar Google Colab con mlflow. 
     </p>  

- **Requisitos de seguridad:**
   
    <p align="justify">
   * Este modelo desea predecir si un paciente tiene VIH (SIDA) o no, por ende, cada vez que se haga una predicción, esta debe ir ligada a un paciente y a su vez, debe existir una forma de ligar la predicción con el paciente, por ende, tendrían que uilizarse datos sensibles como el número de identificación o el nombre del paciente. Entonces, es posible pensar que es necesario que exista un proceso de MFA (Autenticación multifactor) para acceder a la aplicación desde la que va a ser consumido el modelo. 
    </p>  

   <p align="justify">
   * También, es posible pensar en la viavilidad de establecer proceses de enmascaramiento de datos o encriptación, especifícamente para los datos referentes a la identificación del paciente, como número de cédula o sus nombres. 
    </p>  

- **Diagrama de arquitectura:** (imagen que muestra la arquitectura del sistema que se utilizará para desplegar el modelo)

## Código de despliegue

- **Archivo principal:** (nombre del archivo principal que contiene el código de despliegue)
- **Rutas de acceso a los archivos:** (lista de rutas de acceso a los archivos necesarios para el despliegue)
- **Variables de entorno:** (lista de variables de entorno necesarias para el despliegue)

## Documentación del despliegue

- **Instrucciones de instalación:** (instrucciones detalladas para instalar el modelo en la plataforma de despliegue)
- **Instrucciones de configuración:** (instrucciones detalladas para configurar el modelo en la plataforma de despliegue)
- **Instrucciones de uso:** (instrucciones detalladas para utilizar el modelo en la plataforma de despliegue)
- **Instrucciones de mantenimiento:** (instrucciones detalladas para mantener el modelo en la plataforma de despliegue)
