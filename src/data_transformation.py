import pandas as pd
import functions as f
import numpy as np
from sklearn.preprocessing import StandardScaler

def transformation_data(df_players_wrangled, df_leagues_wrangled):
    df_players_transformed = df_players_wrangled
    df_leagues_transformed = df_leagues_wrangled

    # Crear agregaciones importantes
    df_players_transformed['attacking_mean'] = df_players_transformed[['attacking_crossing_sum', 'attacking_finishing_sum', 'attacking_heading_accuracy_sum', 'attacking_short_passing_sum', 'attacking_volleys_sum']].mean(axis=1)
    df_players_transformed['defending_mean'] = df_players_transformed[['defending_marking_sum', 'defending_standing_tackle_sum', 'defending_sliding_tackle_sum']].mean(axis=1)
    df_players_transformed['physical_mean'] = df_players_transformed[['power_jumping_sum', 'power_stamina_sum', 'power_strength_sum', 'power_long_shots_sum']].mean(axis=1)
    df_players_transformed['goalkeeping_mean'] = df_players_transformed[['gk_diving', 'gk_handling', 'gk_kicking', 'gk_reflexes', 'gk_speed', 'gk_positioning']].mean(axis=1)


    # Conteo de posiciones primarios
    df_players_transformed['primary_positions_count'] = df_players_transformed['player_positions'].apply(lambda x: len(x.split(',')))

    # Agregar edad promedio por club
    average_age_per_club = df_players_transformed.groupby('club')['age'].mean().reset_index().rename(columns={'age': 'average_age_per_club'})
    df_players_transformed = df_players_transformed.merge(average_age_per_club, on='club', how='left')

    # Media de value por jugador
    average_value_per_player = df_players_transformed.groupby('long_name')['value_eur'].mean().reset_index().rename(columns={'value_eur': 'average_value_per_player'})
    df_players_transformed = df_players_transformed.merge(average_value_per_player, on='long_name', how='left')

    # Media del sueldo por jugador
    average_wage_per_player = df_players_transformed.groupby('long_name')['wage_eur'].mean().reset_index().rename(columns={'wage_eur': 'average_wage_per_player'})
    df_players_transformed = df_players_transformed.merge(average_wage_per_player, on='long_name', how='left')

    # Lista de variables numericas
    numeric_columns = [ 'age', 'height_cm', 'weight_kg', 'overall', 'potential', 'value_eur', 'wage_eur', 'pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic', 'gk_diving', 'gk_handling', 'gk_kicking', 'gk_reflexes', 'gk_speed', 'gk_positioning', 'attacking_crossing_sum', 'attacking_finishing_sum', 'attacking_heading_accuracy_sum', 'attacking_short_passing_sum', 'attacking_volleys_sum', 'skill_dribbling_sum', 'skill_curve_sum', 'skill_fk_accuracy_sum', 'skill_long_passing_sum', 'skill_ball_control_sum', 'movement_acceleration_sum', 'movement_sprint_speed_sum', 'movement_agility_sum', 'movement_reactions_sum', 'movement_balance_sum', 'power_shot_power_sum', 'power_jumping_sum', 'power_stamina_sum', 'power_strength_sum', 'power_long_shots_sum', 'mentality_aggression_sum', 'mentality_interceptions_sum', 'mentality_positioning_sum', 'mentality_vision_sum', 'mentality_penalties_sum', 'mentality_composure_sum', 'defending_marking_sum', 'defending_standing_tackle_sum', 'defending_sliding_tackle_sum', 'attacking_mean', 'defending_mean', 'physical_mean' ]
    
    # Normalizar y escalar las columnas numericas
    scaler = StandardScaler() 
    df_players_transformed[numeric_columns] = scaler.fit_transform(df_players_transformed[numeric_columns])

    print(df_players_transformed.head(10))
    print(df_leagues_transformed.head(10))

    return df_players_transformed, df_leagues_transformed

