import pandas as pd
import functions as f
import numpy as np

def wrangle_data(df_players_cleaned, df_leagues_cleaned):
    df_players_wrangled = df_players_cleaned
    df_leagues_wrangled = df_leagues_cleaned

    print(df_players_wrangled.head(10))
    print(df_leagues_wrangled.head(10))

    return df_players_wrangled, df_leagues_wrangled