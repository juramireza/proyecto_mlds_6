# Despliegue de modelos

## Infraestructura

- **Nombre del modelo:** final_model 
- **Plataforma de despliegue:** El despliegue se hizo utilizando la herramienta de mlflow
- **Requisitos técnicos:** Se  requieren las siguientes herramientas, que se encuentran en los enlaces que se presentan a continuación: 

   * Software: Se requiere una herramienta para desarrollar en python y sea viable instalar la biblioteca de mlflow. Para este proyecto se empleo el ambiente de google colab, en el que se instaló la librería de mlflow y en conjunto, con la interfaz de mlflow, se hizo el despliegue del modelo. Hay que recordar, que como se empleo Google Colab, para realizar el despliegue del modelo, entonces, también se hizo uso de la herramienta pyngrok, con el objetivo de conectar Google Colab con mlflow. Por último, pero no menos importante se utilizaron herramientas de versionamiento, primero DVC, para versionar los datos, Git con Github para versionar el código y mlflow nuevamente, pero para versionar los modelos. 
     </p>  

    * Entorno de python: https://github.com/juramireza/proyecto_mlds_6/blob/master/mlruns/final_model/f07e5539accd45dea6c796a24f65dd04/artifacts/final_model/python_env.yaml
   

  
    * Bibliotecas: https://github.com/juramireza/proyecto_mlds_6/blob/master/mlruns/final_model/f07e5539accd45dea6c796a24f65dd04/artifacts/final_model/requirements.txt. Para mayor detallar de los requerimientos con relación al entorno de python y las bibliotecas necesarias para realizar el despliegue del modelo, es viable consultarlos en  https://github.com/juramireza/proyecto_mlds_6/tree/master/mlruns/final_model/f07e5539accd45dea6c796a24f65dd04/artifacts/final_model  
 
    
   <p align="justify">
 

- **Requisitos de seguridad:**
   
    <p align="justify">
   *  Este modelo desea predecir si un paciente tiene VIH (SIDA) o no, por ende, cada vez que se haga una predicción, esta debe ir ligada a un paciente y a su vez, debe existir una forma de ligar la predicción con el paciente, por ende, tendrían que uilizarse datos sensibles como el número de identificación o el nombre del paciente. Entonces, es posible pensar que es necesario que exista un proceso de MFA (Autenticación multifactor) para acceder a la aplicación desde la que va a ser consumido el modelo. 
    </p>  

    <p align="justify">
    * También, es posible pensar en la viavilidad de establecer procesos de enmascaramiento de datos o encriptación de estos, especifícamente para los datos referentes a la identificación del paciente, como número de cédula o sus nombres. Con el objetivo, de proteger la identidad del paciente y que solamente, determinados perfiles con ciertos privilegios, tengan la posibilidad de acceder a esta información.   
    </p>  

- **Diagrama de arquitectura:** (imagen que muestra la arquitectura del sistema que se utilizará para desplegar el modelo)

## Código de despliegue

- **Archivo principal:** En esta url https://github.com/juramireza/proyecto_mlds_6/blob/master/scripts/training/final_model_mlflow.ipynb, se encuentra el código, empleado para realizar el despligue del modelo final_model que se construyó con el algoritmo de bosques aleatorios. 
- **Rutas de acceso a los archivos:** Se requieren de las siguientes rutas para realizar el despliegue del modelo:

 * Ruta del repositorio en github, que esta siendo utilizado para versionar el código:https://github.com/juramireza/proyecto_mlds_6   

 * Ruta en la que se encuetra el código para realizar el código del despliegue: https://github.com/juramireza/proyecto_mlds_6/blob/master/scripts/training/final_model_mlflow.ipynb 

- **Variables de entorno:** En la siguiente tabla se enuncian las variables de entorno utilizadas, para el despliegu y el objetivo de cada una de estas.

| Nombre de la variable | Objetivo |
| --- | --- | 
| GITHUB | En esta variable se guarda la ruta del repositorio de Github y el token para conectar Google Colab con Github |
| NGROK_TOKEN | En esta variable se guarda el token de pyngrok, con el fin de hacer la conexión entre Google Colab y la herramienta de mlflow |
| MLFLOW_TRACKING_URI | En esta variable se guarda la ruta http://localhost:5000, para especificar la url del servidor de seguimiento de mlflow |

## Documentación del despliegue

- **Instrucciones de instalación:**

1. Cargar el modelo desde el archivo 

(instrucciones detalladas para instalar el modelo en la plataforma de despliegue)
- **Instrucciones de configuración:** (instrucciones detalladas para configurar el modelo en la plataforma de despliegue)
- **Instrucciones de uso:** (instrucciones detalladas para utilizar el modelo en la plataforma de despliegue)
- **Instrucciones de mantenimiento:** (instrucciones detalladas para mantener el modelo en la plataforma de despliegue)
