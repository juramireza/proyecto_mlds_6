# -*- coding: utf-8 -*-
"""data_acquisition.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vfoAyMTlYx7GqfCtOx83TvLKP9qJhIr4

Instalo dvc y tree
"""

!pip install dvc dvc-gdrive

!apt install tree

import os
from IPython import get_ipython

"""Clono el repositorio donde se aloja el proyecto"""

!git clone "https://github.com/juramireza/proyecto_mlds_6"

!git config --global user.email "jdortizc@unal.edu.co"
!git config --global user.name "jdoc"
!git config --global init.defaultBranch master

!git init

!pip install --user kaggle
!apt-get install unzip

"""Descargo y descomprimo el archivo con los datos en una carpeta llamada "data"
"""

!mkdir 'data'
!kaggle datasets download -d aadarshvelu/aids-virus-infection-prediction
!mv /content/aids-virus-infection-prediction.zip /content/data/data_aids_Clasification.zip
!unzip /content/data/data_aids_Clasification.zip AIDS_Classification.csv -d /content/data/

!tree

!git status

!dvc init

!ls -a

"""Temaño del dataset"""

os.path.getsize("/content/data/AIDS_Classification.csv")

!dvc add data/AIDS_Classification.csv

!ls -a data/

!git add data/.gitignore data/*.csv.dvc

!git status

!git commit -m "Inicializamos dvc y agregamos el dataset descargado de Kaggle"

!git push origin master

import pandas as pd
df = pd.read_csv('/content/data/AIDS_Classification.csv')

df

!git status