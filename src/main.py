import pandas as pd
from data_cleaning import clean_data
from data_wrangling import wrangle_data

#  data cleaning
df_players_cleaned, df_leagues_cleaned = clean_data()

# data wrangling
df_players_wrangled, df_leagues_wrangled = wrangle_data(df_players_cleaned, df_leagues_cleaned)

# Print final result
print('Resultado final:', df_players_wrangled)
