# # Documentación del data transfomation

## Descripción General
El script `transformation_data` transforma y enriquece los datos de jugadores y ligas mediante la creación de nuevas columnas, el cálculo de agregaciones importantes y la normalización de los datos numéricos.

## Importación de Librerías

```python
import pandas as pd
import functions as f
import numpy as np
from sklearn.preprocessing import StandardScaler
```

Se importan las librerías necesarias: `pandas` para manipulación de datos, `functions` para funciones personalizadas, `numpy` para operaciones numéricas y `StandardScaler` de `scikit-learn` para la normalización de datos.

## Definición de la Función

```python
def transformation_data(df_players_wrangled, df_leagues_wrangled):
    ...
```

La función `transformation_data` toma dos argumentos: `df_players_wrangled` y `df_leagues_wrangled`, que son DataFrames de jugadores y ligas ya transformados y preparados.

## Transformación de Datos

```python
    df_players_transformed = df_players_wrangled
    df_leagues_transformed = df_leagues_wrangled
```

Se asignan los DataFrames a nuevas variables para realizar las transformaciones.

## Creación de Agregaciones Importantes

```python
    df_players_transformed['attacking_mean'] = df_players_transformed[['attacking_crossing_sum', 'attacking_finishing_sum', 'attacking_heading_accuracy_sum', 'attacking_short_passing_sum', 'attacking_volleys_sum']].mean(axis=1).round(2)
    df_players_transformed['defending_mean'] = df_players_transformed[['defending_marking_sum', 'defending_standing_tackle_sum', 'defending_sliding_tackle_sum']].mean(axis=1).round(2)
    df_players_transformed['physical_mean'] = df_players_transformed[['power_jumping_sum', 'power_stamina_sum', 'power_strength_sum', 'power_long_shots_sum']].mean(axis=1).round(2)
    df_players_transformed['goalkeeping_mean'] = df_players_transformed[['gk_diving', 'gk_handling', 'gk_kicking', 'gk_reflexes', 'gk_speed', 'gk_positioning']].mean(axis=1).round(2)
```

Se crean nuevas columnas calculando las medias de atributos importantes para ataque, defensa, físico y portería, redondeando los resultados a 2 decimales.

## Conteo de Posiciones Primarias

```python
    df_players_transformed['primary_positions_count'] = df_players_transformed['player_positions'].apply(lambda x: len(x.split(',')))
```

Se agrega una columna que cuenta el número de posiciones primarias de cada jugador.

## Agregar Edad Promedio por Club

```python
    average_age_per_club = df_players_transformed.groupby('club')['age'].mean().reset_index().rename(columns={'age': 'average_age_per_club'})
    df_players_transformed = df_players_transformed.merge(average_age_per_club, on='club', how='left')
```

Se calcula la edad promedio por club y se agrega esta información al DataFrame de jugadores.

## Media de Valor y Sueldo por Jugador

```python
    average_value_per_player = df_players_transformed.groupby('long_name')['value_eur'].mean().reset_index().rename(columns={'value_eur': 'average_value_per_player'})
    df_players_transformed = df_players_transformed.merge(average_value_per_player, on='long_name', how='left')

    average_wage_per_player = df_players_transformed.groupby('long_name')['wage_eur'].mean().reset_index().rename(columns={'wage_eur': 'average_wage_per_player'})
    df_players_transformed = df_players_transformed.merge(average_wage_per_player, on='long_name', how='left')
```

Se calcula la media del valor y sueldo por jugador y se agrega esta información al DataFrame de jugadores.

## Lista de Variables Numéricas

```python
    numeric_columns = [ 'age', 'height_cm', 'weight_kg', 'overall', 'potential', 'value_eur', 'wage_eur', 'pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic', 'gk_diving', 'gk_handling', 'gk_kicking', 'gk_reflexes', 'gk_speed', 'gk_positioning', 'attacking_crossing_sum', 'attacking_finishing_sum', 'attacking_heading_accuracy_sum', 'attacking_short_passing_sum', 'attacking_volleys_sum', 'skill_dribbling_sum', 'skill_curve_sum', 'skill_fk_accuracy_sum', 'skill_long_passing_sum', 'skill_ball_control_sum', 'movement_acceleration_sum', 'movement_sprint_speed_sum', 'movement_agility_sum', 'movement_reactions_sum', 'movement_balance_sum', 'power_shot_power_sum', 'power_jumping_sum', 'power_stamina_sum', 'power_strength_sum', 'power_long_shots_sum', 'mentality_aggression_sum', 'mentality_interceptions_sum', 'mentality_positioning_sum', 'mentality_vision_sum', 'mentality_penalties_sum', 'mentality_composure_sum', 'defending_marking_sum', 'defending_standing_tackle_sum', 'defending_sliding_tackle_sum', 'attacking_mean', 'defending_mean', 'physical_mean' ]
```

Se define una lista de columnas numéricas que serán normalizadas y escaladas.

## Normalización y Escalado de Datos

```python
    scaler = StandardScaler() 
    df_players_transformed[numeric_columns] = scaler.fit_transform(df_players_transformed[numeric_columns])
```

Se utiliza `StandardScaler` para normalizar y escalar las columnas numéricas del DataFrame de jugadores.

## Impresión de Datos Transformados

```python
    print(df_players_transformed.head(10))
    print(df_leagues_transformed.head(10))
```

Se imprimen las primeras 10 filas de los DataFrames de jugadores y ligas transformados para verificación.

## Retorno de DataFrames Transformados

```python
    return df_players_transformed, df_leagues_transformed
```

La función retorna los DataFrames `df_players_transformed` y `df_leagues_transformed` con las transformaciones aplicadas.

---