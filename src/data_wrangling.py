import pandas as pd
import functions as f
import numpy as np

def wrangle_data(df_players_cleaned, df_leagues_cleaned):
    df_players_wrangled = df_players_cleaned
    df_leagues_wrangled = df_leagues_cleaned

    print(df_players_wrangled.head(10))
    print(df_leagues_wrangled.head(10))

    # Crear nuevas columnas (categoricas)
    df_players_wrangled['age_category'] = pd.cut(df_players_wrangled['age'], bins=[0, 20, 30, 40, 100],
                                                 labels=['Joven', 'Optimo', 'Veterano', 'Retirado'])
    df_players_wrangled['overall_category'] = pd.cut(df_players_wrangled['overall'],
                                                     bins=[0, 60, 70, 80, 90, 100],
                                                     labels=['Bajo', 'Promedio', 'Bueno', 'Muy_bueno', 'Excelente'])
    df_players_wrangled['potential_category'] = pd.cut(df_players_wrangled['potential'], 
                                                   bins=[0, 60, 70, 80, 90, 100], 
                                                   labels=['Bajo', 'Promedio', 'Bueno', 'Muy_bueno', 'Excelente'])
    df_players_wrangled['height_category'] = pd.cut(df_players_wrangled['height_cm'], 
                                                    bins=[0, 160, 170, 180, 190, 210], 
                                                    labels=['Muy_bajo', 'Bajo', 'Promedio', 'Alto', 'Muy_alto'])
    df_players_wrangled['weight_category'] = pd.cut(df_players_wrangled['weight_kg'], 
                                                bins=[0, 60, 70, 80, 90, 110], 
                                                labels=['Muy_ligero', 'Ligero', 'Promedio', 'Pesado', 'Muy_pesado'])
    df_players_wrangled['pace_category'] = pd.cut(df_players_wrangled['pace'], 
                                              bins=[0, 40, 60, 80, 90, 100], 
                                              labels=['Muy_lento', 'Lento', 'Promedio', 'Rapido', 'Muy_rapido'])
    df_players_wrangled['shooting_category'] = pd.cut(df_players_wrangled['shooting'], 
                                                  bins=[0, 40, 60, 80, 90, 100], 
                                                  labels=['Muy_bajo', 'Bajo', 'Promedio', 'Alto', 'Muy_alto'])
    df_players_wrangled['passing_category'] = pd.cut(df_players_wrangled['passing'], 
                                                 bins=[0, 40, 60, 80, 90, 100], 
                                                 labels=['Muy_bajo', 'Bajo', 'Promedio', 'Alto', 'Muy_alto'])

    # Eliminamos columnas que ya no necesitamos
    # Lista de columnas a eliminar 
    columns_to_remove = ['attacking_crossing','attacking_finishing','attacking_heading_accuracy','attacking_short_passing','attacking_volleys','skill_dribbling','skill_curve','skill_fk_accuracy','skill_long_passing','skill_ball_control','movement_acceleration','movement_sprint_speed','movement_agility','movement_reactions','movement_balance','power_shot_power','power_jumping','power_stamina','power_strength','power_long_shots','mentality_aggression','mentality_interceptions','mentality_positioning','mentality_vision','mentality_penalties','mentality_composure','defending_marking','defending_standing_tackle','defending_sliding_tackle','goalkeeping_diving','goalkeeping_handling','goalkeeping_kicking','goalkeeping_positioning','goalkeeping_reflexes','ls','st','rs','lw','lf','cf','rf','rw','lam','cam','ram','lm','lcm','cm','rcm','rm','lwb','ldm','cdm','rdm','rwb','lb','lcb','cb','rcb','rb']

    # Operar filas con operaciones numericas - con bucle
    for col in columns_to_remove:
        df_players_wrangled[f'{col}_sum'] = df_players_wrangled[col].apply(f.convert_and_sum)

    # Eliminar las columnas
    df_players_wrangled = df_players_wrangled.drop(columns = columns_to_remove)

    return df_players_wrangled, df_leagues_wrangled

