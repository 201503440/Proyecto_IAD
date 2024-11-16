import pandas as pd
from data_cleaning import clean_data
from data_wrangling import wrangle_data
from data_transformation import transformation_data
import functions as f

#  data cleaning
df_players_cleaned, df_leagues_cleaned = clean_data()

# data wrangling
df_players_wrangled, df_leagues_wrangled = wrangle_data(df_players_cleaned, df_leagues_cleaned)

# data wrangling
df_players_transformed, df_leagues_transformed = transformation_data(df_players_wrangled, df_leagues_wrangled)

# Guardar el resultado final
f.save_dataset_to_csv(dataset=df_players_transformed, filename='df_leaguesFinal.csv')
f.save_dataset_to_csv(dataset=df_leagues_transformed, filename='df_playersFinal.csv')
print('Resultado final, guardado.')
