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

    # Operar filas con operaciones numericas
    df_players_wrangled['attacking_crossing_sum'] = df_players_wrangled['attacking_crossing'].apply(f.convert_and_sum)
    df_players_wrangled['attacking_finishing_sum'] = df_players_wrangled['attacking_finishing'].apply(f.convert_and_sum)
    df_players_wrangled['attacking_heading_accuracy_sum'] = df_players_wrangled['attacking_heading_accuracy'].apply(f.convert_and_sum)
    df_players_wrangled['attacking_short_passing_sum'] = df_players_wrangled['attacking_short_passing'].apply(f.convert_and_sum)
    df_players_wrangled['attacking_volleys_sum'] = df_players_wrangled['attacking_volleys'].apply(f.convert_and_sum)
    df_players_wrangled['skill_dribbling_sum'] = df_players_wrangled['skill_dribbling'].apply(f.convert_and_sum)
    df_players_wrangled['skill_curve_sum'] = df_players_wrangled['skill_curve'].apply(f.convert_and_sum)
    df_players_wrangled['skill_fk_accuracy_sum'] = df_players_wrangled['skill_fk_accuracy'].apply(f.convert_and_sum)
    df_players_wrangled['skill_long_passing_sum'] = df_players_wrangled['skill_long_passing'].apply(f.convert_and_sum)
    df_players_wrangled['skill_ball_control_sum'] = df_players_wrangled['skill_ball_control'].apply(f.convert_and_sum)
    df_players_wrangled['movement_acceleration_sum'] = df_players_wrangled['movement_acceleration'].apply(f.convert_and_sum)
    df_players_wrangled['movement_sprint_speed_sum'] = df_players_wrangled['movement_sprint_speed'].apply(f.convert_and_sum)
    df_players_wrangled['movement_agility_sum'] = df_players_wrangled['movement_agility'].apply(f.convert_and_sum)
    df_players_wrangled['movement_reactions_sum'] = df_players_wrangled['movement_reactions'].apply(f.convert_and_sum)
    df_players_wrangled['movement_balance_sum'] = df_players_wrangled['movement_balance'].apply(f.convert_and_sum)
    df_players_wrangled['power_shot_power_sum'] = df_players_wrangled['power_shot_power'].apply(f.convert_and_sum)
    df_players_wrangled['power_jumping_sum'] = df_players_wrangled['power_jumping'].apply(f.convert_and_sum)
    df_players_wrangled['power_stamina_sum'] = df_players_wrangled['power_stamina'].apply(f.convert_and_sum)
    df_players_wrangled['power_strength_sum'] = df_players_wrangled['power_strength'].apply(f.convert_and_sum)
    df_players_wrangled['power_long_shots_sum'] = df_players_wrangled['power_long_shots'].apply(f.convert_and_sum)
    df_players_wrangled['mentality_aggression_sum'] = df_players_wrangled['mentality_aggression'].apply(f.convert_and_sum)
    df_players_wrangled['mentality_interceptions_sum'] = df_players_wrangled['mentality_interceptions'].apply(f.convert_and_sum)
    df_players_wrangled['mentality_positioning_sum'] = df_players_wrangled['mentality_positioning'].apply(f.convert_and_sum)
    df_players_wrangled['mentality_vision_sum'] = df_players_wrangled['mentality_vision'].apply(f.convert_and_sum)
    df_players_wrangled['mentality_penalties_sum'] = df_players_wrangled['mentality_penalties'].apply(f.convert_and_sum)
    df_players_wrangled['mentality_composure_sum'] = df_players_wrangled['mentality_composure'].apply(f.convert_and_sum)
    df_players_wrangled['defending_marking_sum'] = df_players_wrangled['defending_marking'].apply(f.convert_and_sum)
    df_players_wrangled['defending_standing_tackle_sum'] = df_players_wrangled['defending_standing_tackle'].apply(f.convert_and_sum)
    df_players_wrangled['defending_sliding_tackle_sum'] = df_players_wrangled['defending_sliding_tackle'].apply(f.convert_and_sum)
    df_players_wrangled['goalkeeping_diving_sum'] = df_players_wrangled['goalkeeping_diving'].apply(f.convert_and_sum)
    df_players_wrangled['goalkeeping_handling_sum'] = df_players_wrangled['goalkeeping_handling'].apply(f.convert_and_sum)
    df_players_wrangled['goalkeeping_kicking_sum'] = df_players_wrangled['goalkeeping_kicking'].apply(f.convert_and_sum)
    df_players_wrangled['goalkeeping_positioning_sum'] = df_players_wrangled['goalkeeping_positioning'].apply(f.convert_and_sum)
    df_players_wrangled['goalkeeping_reflexes_sum'] = df_players_wrangled['goalkeeping_reflexes'].apply(f.convert_and_sum)
    df_players_wrangled['ls_sum'] = df_players_wrangled['ls'].apply(f.convert_and_sum)
    df_players_wrangled['st_sum'] = df_players_wrangled['st'].apply(f.convert_and_sum)
    df_players_wrangled['rs_sum'] = df_players_wrangled['rs'].apply(f.convert_and_sum)
    df_players_wrangled['lw_sum'] = df_players_wrangled['lw'].apply(f.convert_and_sum)
    df_players_wrangled['lf_sum'] = df_players_wrangled['lf'].apply(f.convert_and_sum)
    df_players_wrangled['cf_sum'] = df_players_wrangled['cf'].apply(f.convert_and_sum)
    df_players_wrangled['rf_sum'] = df_players_wrangled['rf'].apply(f.convert_and_sum)
    df_players_wrangled['rw_sum'] = df_players_wrangled['rw'].apply(f.convert_and_sum)
    df_players_wrangled['lam_sum'] = df_players_wrangled['lam'].apply(f.convert_and_sum)
    df_players_wrangled['cam_sum'] = df_players_wrangled['cam'].apply(f.convert_and_sum)
    df_players_wrangled['ram_sum'] = df_players_wrangled['ram'].apply(f.convert_and_sum)
    df_players_wrangled['lm_sum'] = df_players_wrangled['lm'].apply(f.convert_and_sum)
    df_players_wrangled['lcm_sum'] = df_players_wrangled['lcm'].apply(f.convert_and_sum)
    df_players_wrangled['cm_sum'] = df_players_wrangled['cm'].apply(f.convert_and_sum)
    df_players_wrangled['rcm_sum'] = df_players_wrangled['rcm'].apply(f.convert_and_sum)
    df_players_wrangled['rm_sum'] = df_players_wrangled['rm'].apply(f.convert_and_sum)
    df_players_wrangled['lwb_sum'] = df_players_wrangled['lwb'].apply(f.convert_and_sum)
    df_players_wrangled['ldm_sum'] = df_players_wrangled['ldm'].apply(f.convert_and_sum)
    df_players_wrangled['cdm_sum'] = df_players_wrangled['cdm'].apply(f.convert_and_sum)
    df_players_wrangled['rdm_sum'] = df_players_wrangled['rdm'].apply(f.convert_and_sum)
    df_players_wrangled['rwb_sum'] = df_players_wrangled['rwb'].apply(f.convert_and_sum)
    df_players_wrangled['lb_sum'] = df_players_wrangled['lb'].apply(f.convert_and_sum)
    df_players_wrangled['lcb_sum'] = df_players_wrangled['lcb'].apply(f.convert_and_sum)
    df_players_wrangled['cb_sum'] = df_players_wrangled['cb'].apply(f.convert_and_sum)
    df_players_wrangled['rcb_sum'] = df_players_wrangled['rcb'].apply(f.convert_and_sum)
    df_players_wrangled['rb_sum'] = df_players_wrangled['rb'].apply(f.convert_and_sum)

    # Eliminamos columnas que ya no necesitamos
    # Lista de columnas a eliminar 
    columns_to_remove = ['attacking_crossing','attacking_finishing','attacking_heading_accuracy','attacking_short_passing','attacking_volleys','skill_dribbling','skill_curve','skill_fk_accuracy','skill_long_passing','skill_ball_control','movement_acceleration','movement_sprint_speed','movement_agility','movement_reactions','movement_balance','power_shot_power','power_jumping','power_stamina','power_strength','power_long_shots','mentality_aggression','mentality_interceptions','mentality_positioning','mentality_vision','mentality_penalties','mentality_composure','defending_marking','defending_standing_tackle','defending_sliding_tackle','goalkeeping_diving','goalkeeping_handling','goalkeeping_kicking','goalkeeping_positioning','goalkeeping_reflexes','ls','st','rs','lw','lf','cf','rf','rw','lam','cam','ram','lm','lcm','cm','rcm','rm','lwb','ldm','cdm','rdm','rwb','lb','lcb','cb','rcb','rb']
    
    # Eliminar las columnas
    df_players_wrangled = df_players_wrangled.drop(columns = columns_to_remove)

    return df_players_wrangled, df_leagues_wrangled

