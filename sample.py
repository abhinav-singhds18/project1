import numpy as np
import pandas as pd
import csv

data_df = pd.read_csv("C:/Users/abhinavlenovo/Desktop/assignment/data.csv")
metadata_df = pd.read_csv("C:/Users/abhinavlenovo/Desktop/assignment/metadata.csv")

merged_df = pd.merge( data_df, metadata_df ,how = 'outer',on = 'time_series_code')
data_df.columns
metadata_df.columns
