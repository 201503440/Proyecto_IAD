# # Documentación del data wrangling

## Descripción General
El script `wrangle_data` se utiliza para transformar y limpiar datos de jugadores y ligas, creando nuevas columnas categóricas y realizando operaciones de suma en varias columnas. 

## Importación de Librerías

```python
import pandas as pd
import functions as f
import numpy as np
```

Se importan las librerías necesarias: `pandas` para manipulación de datos, `functions` para funciones personalizadas, y `numpy` para operaciones numéricas.

## Definición de la Función

```python
def wrangle_data(df_players_cleaned, df_leagues_cleaned):
    ...
```

La función `wrangle_data` toma dos argumentos: `df_players_cleaned` y `df_leagues_cleaned`, que son DataFrames de jugadores y ligas ya limpiados.

## Wrangling de Datos

```python
    df_players_wrangled = df_players_cleaned
    df_leagues_wrangled = df_leagues_cleaned

    print(df_players_wrangled.head(10))
    print(df_leagues_wrangled.head(10))
```

Los DataFrames se asignan a nuevas variables y se imprimen las primeras 10 filas para verificar los datos.

## Creación de Nuevas Columnas (Categorías)

```python
    df_players_wrangled['age_category'] = pd.cut(df_players_wrangled['age'], bins=[0, 20, 30, 40, 100],
                                                 labels=['Joven', 'Optimo', 'Veterano', 'Retirado'])
    df_players_wrangled['overall_category'] = pd.cut(df_players_wrangled['overall'],
                                                     bins=[0, 60, 70, 80, 90, 100],
                                                     labels=['Bajo', 'Promedio', 'Bueno', 'Muy_bueno', 'Excelente'])
    ...
```

Se crean nuevas columnas categóricas para `age`, `overall`, `potential`, `height`, `weight`, `pace`, `shooting`, y `passing` usando la función `pd.cut()` de `pandas`.

## Eliminación de Columnas No Necesarias

```python
    columns_to_remove = ['attacking_crossing','attacking_finishing','attacking_heading_accuracy',...,'rb']
```

Se define una lista `columns_to_remove` que contiene las columnas que serán eliminadas.

## Operaciones Numéricas en Columnas

```python
    for col in columns_to_remove:
        df_players_wrangled[f'{col}_sum'] = df_players_wrangled[col].apply(f.convert_and_sum)
```

Para cada columna en `columns_to_remove`, se aplica la función `convert_and_sum` para convertir y sumar los valores.

## Eliminación de Columnas

```python
    df_players_wrangled = df_players_wrangled.drop(columns = columns_to_remove)
```

Se eliminan las columnas listadas en `columns_to_remove`.

## Retorno de DataFrames

```python
    return df_players_wrangled, df_leagues_wrangled
```

La función retorna los DataFrames transformados `df_players_wrangled` y `df_leagues_wrangled`.

---
