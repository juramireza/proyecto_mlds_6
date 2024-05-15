import seaborn as sns
import matplotlib.pyplot as plt
def graficos_con_hue(dataframe, hue=None):
    sns.set(style='whitegrid')
    columnas_numericas = dataframe.select_dtypes(include=['number']).columns
    num_cols = len(columnas_numericas)
    fig, axes = plt.subplots(num_cols, 2, figsize=(10, 4 * num_cols))
    for i, col in enumerate(columnas_numericas):
      # Boxplot en la primera columna de subplots
      sns.boxplot(data=dataframe, y=col, ax=axes[i, 0], hue=dataframe[hue] if hue else None)
      axes[i, 0].set_title('Boxplot')

      # Histograma con KDE en la segunda columna de subplots
      sns.histplot(data=dataframe, x=col, kde=True, ax=axes[i, 1], hue=dataframe[hue] if hue else None)
      axes[i, 1].set_title('Histograma')

      # KDE en la tercera columna de subplots
      #sns.kdeplot(data=dataframe, x=col, ax=axes[i, 2], fill=True, color="skyblue", hue=dataframe[hue] if hue else None)
      #axes[i, 2].set_title('KDE')

    # Ajustar la disposición de los subplots para evitar solapamientos
    plt.tight_layout()
    plt.show()
