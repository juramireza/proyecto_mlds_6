import pandas as pd
def filtrar_outliers_por_categoria(dataframe, columnas, factor, categoria_col):
    # Crear un DataFrame vacío para almacenar los resultados
    df_filtrado = pd.DataFrame()

    # Procesar cada grupo categórico por separado
    for grupo in dataframe[categoria_col].unique():
        # Filtrar el DataFrame original por cada categoría
        df_grupo = dataframe[dataframe[categoria_col] == grupo]

        # Realizar la limpieza de outliers en el grupo actual
        for col in columnas:
            if col in df_grupo.columns:
                f1 = df_grupo[col].quantile(0.25)
                f3 = df_grupo[col].quantile(0.75)
                IQR = f3 - f1
                limite_inferior = f1 - factor * IQR
                limite_superior = f3 + factor * IQR
                df_grupo = df_grupo[(df_grupo[col] >= limite_inferior) & (df_grupo[col] <= limite_superior)]

        # Concatenar el grupo limpio al DataFrame final
        df_filtrado = pd.concat([df_filtrado, df_grupo], ignore_index=True)

    return df_filtrado
