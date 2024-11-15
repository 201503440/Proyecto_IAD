# Documentación del proceso de limpieza y preparación de datos en Python

Este documento describe el proceso completo de limpieza y preparación de dos conjuntos de datos en formato CSV: uno con información de jugadores y otro con información de ligas. El objetivo es asegurar que el código proporcionado sea reproducible en cualquier entorno de desarrollo.

## Requisitos previos

1. **Librerías necesarias**:
   - `pandas`: para manejar y manipular datos en formato DataFrame.
   - `functions` (archivo local `functions.py`): que debe contener funciones personalizadas, como `save_dataset_to_csv`.
   - `numpy`: para realizar operaciones con arrays y matrices, aunque no se utiliza directamente en el código.
   
   Instalar dependencias:
   ```bash
   pip install pandas numpy
   ```

2. **Archivos CSV necesarios**:
   - `players_15.csv`
   - `players_16.csv`
   - `players_17.csv`
   - `players_18.csv`
   - `players_19.csv`
   - `players_20.csv`
   - `teams_and_leagues.csv`
   
   Los archivos deben estar ubicados en la carpeta `../data/`.

## Descripción del código

### 1. Carga de los datos

Primero, se cargan los datos de los jugadores y las ligas desde los archivos CSV:

```python
import pandas as pd
import functions as f
import numpy as np

# Cargar los archivos de jugadores
df1 = pd.read_csv('../data/players_15.csv')
df2 = pd.read_csv('../data/players_16.csv')
df3 = pd.read_csv('../data/players_17.csv')
df4 = pd.read_csv('../data/players_18.csv')
df5 = pd.read_csv('../data/players_19.csv')
df6 = pd.read_csv('../data/players_20.csv')

# Concatenar los archivos de jugadores en un solo DataFrame
df_players = pd.concat([df1, df2, df3, df4, df5, df6], ignore_index=True)

# Cargar el archivo de ligas
df_leagues = pd.read_csv('../data/teams_and_leagues.csv')
```

### 2. Eliminación de registros duplicados

A continuación, se eliminan los registros duplicados basándose en el campo `sofifa_id` (un identificador único para cada jugador):

```python
df_players = df_players.drop_duplicates(subset='sofifa_id')
```

### 3. Comprobación de valores nulos

Es fundamental verificar la presencia de valores nulos en ambos conjuntos de datos:

```python
# Verificar valores nulos en ambos datasets
print(len(df_players))
print(df_players.isnull().sum())
print(len(df_leagues))
print(df_leagues.isnull().sum())
```

### 4. Descripción y tipo de datos

Es importante revisar la descripción estadística y los tipos de datos de los DataFrames:

```python
df_players.describe()
df_leagues.describe()

df_players.dtypes
df_leagues.dtypes
```

### 5. Asignación de tipos de datos específicos

Para asegurar la consistencia, se asignan tipos de datos específicos a las columnas de `df_players` y `df_leagues`, además de rellenar los valores nulos:

```python
df_players['sofifa_id'] = df_players['sofifa_id'].fillna(0).astype(int)
df_players['player_url'] = df_players['player_url'].fillna('UNKNOWN').astype(str)
df_players['short_name'] = df_players['short_name'].fillna('UNKNOWN').astype(str)
# Repetir para otras columnas...
df_players['cf'] = df_players['cf'].fillna('UNKNOWN').astype(str)
df_players['rf'] = df_players['rf'].fillna('UNKNOWN').astype(str)
df_players['rw'] = df_players['rw'].fillna('UNKNOWN').astype(str)
# Más columnas de jugadores...
```

En el caso de `df_leagues`, se realiza el mismo proceso de conversión y asignación de valores:

```python
df_leagues['url'] = df_leagues['url'].fillna(0).astype(int)
df_leagues['league_name'] = df_leagues['league_name'].fillna('UNKNOWN').astype(str)
```

### 6. Limpieza de espacios y estandarización

Para mantener una consistencia en el formato de los datos, se eliminan los espacios extra al inicio y final de las cadenas de texto, además de convertir todo el texto a mayúsculas:

```python
df_players = df_players.applymap(lambda x: x.strip().upper() if isinstance(x, str) and not x.startswith(('http', 'https')) else x)
df_leagues = df_leagues.applymap(lambda x: x.strip().upper() if isinstance(x, str) else x)
```

### 7. Verificación de los cambios

Después de aplicar las transformaciones, es recomendable verificar la estructura de los datos y los valores nulos restantes:

```python
print("Vista previa de df_players:")
print(df_players.head())

print("\nInformación general de df_players:")
print(df_players.info())

print("\nVista previa de df_leagues:")
print(df_leagues.head())

print("\nInformación general de df_leagues:")
print(df_leagues.info())

print("\nValores nulos en df_players:\n", df_players.isnull().sum())
print("\nValores nulos en df_leagues:\n", df_leagues.isnull().sum())
```

### 8. Guardado de los datos procesados

Finalmente, se guardan los conjuntos de datos limpios y preparados en archivos CSV:

```python
f.save_dataset_to_csv(dataset=df_leagues, filename='df_leagues2.csv')
f.save_dataset_to_csv(dataset=df_players, filename='df_players2.csv')
```

El código depende de la función `save_dataset_to_csv` definida en el archivo `functions.py`, que se espera guarde el DataFrame en un archivo CSV.

### 9. Consideraciones adicionales

- **Asegurar la disponibilidad de archivos**: Asegúrate de que todos los archivos CSV necesarios estén presentes en la ruta indicada (`../data/`).
- **Manejo de valores nulos**: Se asignan valores predeterminados (`UNKNOWN`, `0`, etc.) a las columnas con valores nulos para evitar errores al trabajar con los datos.
- **Estandarización**: Convertir todas las cadenas de texto a mayúsculas y eliminar espacios asegura que no haya inconsistencias en los datos.

## Conclusión

Este script realiza un proceso de limpieza y transformación de datos para asegurar que los conjuntos de datos de jugadores y ligas estén en un formato consistente y listo para su análisis o uso posterior. Siguiendo estos pasos en cualquier entorno con los archivos adecuados, se garantizará la reproducibilidad del proceso.