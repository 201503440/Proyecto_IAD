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

# Concatenar los archivos de jugadores
df_players = pd.concat([df1, df2, df3, df4, df5, df6], ignore_index=True)

# Cargar el archivo de ligas 
df_leagues = pd.read_csv('../data/teams_and_leagues.csv')

# print(df_players.head(10))
# print(df_leagues.head(10)) # Lineas comentadas para no ejecutarlas cada ver que se ejecuta el script

# Eliminaremos registros duplicados segun campo sofifa_id
df_players = df_players.drop_duplicates(subset='sofifa_id')

# Verificar los valores nulos
print(len(df_players))
print(df_players.isnull().sum())
print(len(df_leagues))
print(df_leagues.isnull().sum())

# Verificar y corregir tipos de datos
df_players.describe()
df_leagues.describe()

df_players.dtypes
df_leagues.dtypes

# f.save_dataset_to_csv(dataset=df_players, filename='df_players.csv') # Linea debug

# Darle un tipo de dato especifico a cada columna para mantener un orden
df_players['sofifa_id'] = df_players['sofifa_id'].fillna(0).astype(int)
df_players['player_url'] = df_players['player_url'].fillna('UNKNOWN').astype(str)
df_players['short_name'] = df_players['short_name'].fillna('UNKNOWN').astype(str)
df_players['long_name'] = df_players['long_name'].fillna('UNKNOWN').astype(str)
df_players['age'] = df_players['age'].fillna(0).astype(int)
df_players['dob'] = pd.to_datetime(df_players['dob'], errors='coerce').dt.date
df_players['height_cm'] = df_players['height_cm'].fillna(0).astype(int)
df_players['weight_kg'] = df_players['weight_kg'].fillna(0).astype(int)
df_players['nationality'] = df_players['nationality'].fillna('UNKNOWN').astype(str)
df_players['club'] = df_players['club'].fillna('UNKNOWN').astype(str)
df_players['overall'] = df_players['overall'].fillna(0).astype(int)
df_players['potential'] = df_players['potential'].fillna(0).astype(int)
df_players['value_eur'] = df_players['value_eur'].fillna(0).astype(int)
df_players['wage_eur'] = df_players['wage_eur'].fillna(0).astype(int)
df_players['player_positions'] = df_players['player_positions'].fillna('UNKNOWN').astype(str)
df_players['preferred_foot'] = df_players['preferred_foot'].fillna('UNKNOWN').astype(str)
df_players['international_reputation'] = df_players['international_reputation'].fillna(0).astype(int)
df_players['weak_foot'] = df_players['weak_foot'].fillna(0).astype(int)
df_players['skill_moves'] = df_players['skill_moves'].fillna(0).astype(int)
df_players['work_rate'] = df_players['work_rate'].fillna('UNKNOWN').astype(str)
df_players['body_type'] = df_players['body_type'].fillna('UNKNOWN').astype(str)
df_players['real_face'] = df_players['real_face'].fillna('UNKNOWN').astype(str)

df_players['release_clause_eur'] = df_players['release_clause_eur'].fillna(0)
df_players['release_clause_eur'] = df_players['release_clause_eur'].replace([np.inf, -np.inf], 0)
df_players['release_clause_eur'] = df_players['release_clause_eur'].astype(int)

df_players['player_tags'] = df_players['player_tags'].fillna('UNKNOWN').astype(str)
df_players['team_position'] = df_players['team_position'].fillna('UNKNOWN').astype(str)
df_players['team_jersey_number'] = df_players['team_jersey_number'].fillna(0).astype(int)
df_players['loaned_from'] = df_players['loaned_from'].fillna('UNKNOWN').astype(str)
df_players['joined'] = pd.to_datetime(df_players['joined'], errors='coerce').dt.date
df_players['contract_valid_until'] = df_players['contract_valid_until'].fillna(0).astype(int)
df_players['nation_position'] = df_players['nation_position'].fillna(0).fillna('UNKNOWN').astype(str)
df_players['nation_jersey_number'] = df_players['nation_jersey_number'].fillna(0).astype(int)
df_players['pace'] = df_players['pace'].fillna(0).astype(int)
df_players['shooting'] = df_players['shooting'].fillna(0).astype(int)
df_players['passing'] = df_players['passing'].fillna(0).astype(int)
df_players['dribbling'] = df_players['dribbling'].fillna(0).astype(int)
df_players['defending'] = df_players['defending'].fillna(0).astype(int)
df_players['physic'] = df_players['physic'].fillna(0).astype(int)
df_players['gk_diving'] = df_players['gk_diving'].fillna(0).astype(int)
df_players['gk_handling'] = df_players['gk_handling'].fillna(0).astype(int)
df_players['gk_kicking'] = df_players['gk_kicking'].fillna(0).astype(int)
df_players['gk_reflexes'] = df_players['gk_reflexes'].fillna(0).astype(int)
df_players['gk_speed'] = df_players['gk_speed'].fillna(0).astype(int)
df_players['gk_positioning'] = df_players['gk_positioning'].fillna(0).astype(int)
df_players['player_traits'] = df_players['player_traits'].fillna('UNKNOWN').astype(str)
df_players['attacking_crossing'] = df_players['attacking_crossing'].fillna(0).fillna('UNKNOWN').astype(str)
df_players['attacking_finishing'] = df_players['attacking_finishing'].fillna(0).fillna('UNKNOWN').astype(str)
df_players['attacking_heading_accuracy'] = df_players['attacking_heading_accuracy'].fillna(0).fillna('UNKNOWN').astype(str)
df_players['attacking_short_passing'] = df_players['attacking_short_passing'].fillna(0).fillna('UNKNOWN').astype(str)
df_players['attacking_volleys'] = df_players['attacking_volleys'].fillna(0).fillna('UNKNOWN').astype(str)
df_players['skill_dribbling'] = df_players['skill_dribbling'].fillna(0).fillna('UNKNOWN').astype(str)
df_players['skill_curve'] = df_players['skill_curve'].fillna(0).fillna('UNKNOWN').astype(str)
df_players['skill_fk_accuracy'] = df_players['skill_fk_accuracy'].fillna(0).fillna('UNKNOWN').astype(str)
df_players['skill_long_passing'] = df_players['skill_long_passing'].fillna(0).fillna('UNKNOWN').astype(str)
df_players['skill_ball_control'] = df_players['skill_ball_control'].fillna(0).fillna('UNKNOWN').astype(str)
df_players['movement_acceleration'] = df_players['movement_acceleration'].fillna(0).fillna('UNKNOWN').astype(str)
df_players['movement_sprint_speed'] = df_players['movement_sprint_speed'].fillna(0).fillna('UNKNOWN').astype(str)
df_players['movement_agility'] = df_players['movement_agility'].fillna(0).fillna('UNKNOWN').astype(str)
df_players['movement_reactions'] = df_players['movement_reactions'].fillna(0).fillna('UNKNOWN').astype(str)
df_players['movement_balance'] = df_players['movement_balance'].fillna(0).fillna('UNKNOWN').astype(str)
df_players['power_shot_power'] = df_players['power_shot_power'].fillna(0).fillna('UNKNOWN').astype(str)
df_players['power_jumping'] = df_players['power_jumping'].fillna(0).fillna('UNKNOWN').astype(str)
df_players['power_stamina'] = df_players['power_stamina'].fillna(0).fillna('UNKNOWN').astype(str)
df_players['power_strength'] = df_players['power_strength'].fillna(0).fillna('UNKNOWN').astype(str)
df_players['power_long_shots'] = df_players['power_long_shots'].fillna(0).fillna('UNKNOWN').astype(str)
df_players['mentality_aggression'] = df_players['mentality_aggression'].fillna(0).fillna('UNKNOWN').astype(str)
df_players['mentality_interceptions'] = df_players['mentality_interceptions'].fillna(0).fillna('UNKNOWN').astype(str)
df_players['mentality_positioning'] = df_players['mentality_positioning'].fillna(0).fillna('UNKNOWN').astype(str)
df_players['mentality_vision'] = df_players['mentality_vision'].fillna(0).fillna('UNKNOWN').astype(str)
df_players['mentality_penalties'] = df_players['mentality_penalties'].fillna(0).fillna('UNKNOWN').astype(str)
df_players['mentality_composure'] = df_players['mentality_composure'].fillna(0).fillna('UNKNOWN').astype(str)
df_players['defending_marking'] = df_players['defending_marking'].fillna(0).fillna('UNKNOWN').astype(str)
df_players['defending_standing_tackle'] = df_players['defending_standing_tackle'].fillna(0).fillna('UNKNOWN').astype(str)
df_players['defending_sliding_tackle'] = df_players['defending_sliding_tackle'].fillna(0).fillna('UNKNOWN').astype(str)
df_players['goalkeeping_diving'] = df_players['goalkeeping_diving'].fillna(0).fillna('UNKNOWN').astype(str)
df_players['goalkeeping_handling'] = df_players['goalkeeping_handling'].fillna(0).fillna('UNKNOWN').astype(str)
df_players['goalkeeping_kicking'] = df_players['goalkeeping_kicking'].fillna(0).fillna('UNKNOWN').astype(str)
df_players['goalkeeping_positioning'] = df_players['goalkeeping_positioning'].fillna(0).fillna('UNKNOWN').astype(str)
df_players['goalkeeping_reflexes'] = df_players['goalkeeping_reflexes'].fillna(0).fillna('UNKNOWN').astype(str)
df_players['ls'] = df_players['ls'].fillna('UNKNOWN').astype(str)
df_players['st'] = df_players['st'].fillna('UNKNOWN').astype(str)
df_players['rs'] = df_players['rs'].fillna('UNKNOWN').astype(str)
df_players['lw'] = df_players['lw'].fillna('UNKNOWN').astype(str)
df_players['lf'] = df_players['lf'].fillna('UNKNOWN').astype(str)
df_players['cf'] = df_players['cf'].fillna('UNKNOWN').astype(str)
df_players['rf'] = df_players['rf'].fillna('UNKNOWN').astype(str)
df_players['rw'] = df_players['rw'].fillna('UNKNOWN').astype(str)
df_players['lam'] = df_players['lam'].fillna('UNKNOWN').astype(str)
df_players['cam'] = df_players['cam'].fillna('UNKNOWN').astype(str)
df_players['ram'] = df_players['ram'].fillna('UNKNOWN').astype(str)
df_players['lm'] = df_players['lm'].fillna('UNKNOWN').astype(str)
df_players['lcm'] = df_players['lcm'].fillna('UNKNOWN').astype(str)
df_players['cm'] = df_players['cm'].fillna('UNKNOWN').astype(str)
df_players['rcm'] = df_players['rcm'].fillna('UNKNOWN').astype(str)
df_players['rm'] = df_players['rm'].fillna('UNKNOWN').astype(str)
df_players['lwb'] = df_players['lwb'].fillna('UNKNOWN').astype(str)
df_players['ldm'] = df_players['ldm'].fillna('UNKNOWN').astype(str)
df_players['cdm'] = df_players['cdm'].fillna('UNKNOWN').astype(str)
df_players['rdm'] = df_players['rdm'].fillna('UNKNOWN').astype(str)
df_players['rwb'] = df_players['rwb'].fillna('UNKNOWN').astype(str)
df_players['lb'] = df_players['lb'].fillna('UNKNOWN').astype(str)
df_players['lcb'] = df_players['lcb'].fillna('UNKNOWN').astype(str)
df_players['cb'] = df_players['cb'].fillna('UNKNOWN').astype(str)
df_players['rcb'] = df_players['rcb'].fillna('UNKNOWN').astype(str)
df_players['rb'] = df_players['rb'].fillna('UNKNOWN').astype(str)

# print(df_players['nationality'].value_counts()) #Validar algunos valores

df_leagues['url'] = df_leagues['url'].fillna(0).astype(int)
df_leagues['league_name'] = df_leagues['league_name'].fillna('UNKNOWN').astype(str)

# Eliminar espacios al inicio y final de todos los valores de tipo str
# Convertir todos los campos de tipo str a mayusculas para tener un estandar
df_players = df_players.applymap(lambda x: x.strip().upper() if isinstance(x, str) and not x.startswith(('http', 'https')) else x)
df_leagues = df_leagues.applymap(lambda x: x.strip().upper() if isinstance(x, str) else x)

# Validamos informacion luego de los casteos 
print("Vista previa de df_players:")
print(df_players.head())
print("\nInformacion general de df_players:")
print(df_players.info())

print("\nVista previa de df_leagues:")
print(df_leagues.head())
print("\nInformacion general de df_leagues:")
print(df_leagues.info())


print("\nValores nulos en df_players:\n", df_players.isnull().sum())
print("\nValores nulos en df_leagues:\n", df_leagues.isnull().sum())

# Escribir los archivos despues de las limpiezas
f.save_dataset_to_csv(dataset=df_leagues, filename='df_leagues2.csv')
f.save_dataset_to_csv(dataset=df_players, filename='df_players2.csv')
