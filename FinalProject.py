#!/usr/bin/env python3
import os

# Libraries needed for the tutorial
import pandas as pd
import requests
import io
    
# Downloading the csv file from your GitHub account

url = "https://raw.githubusercontent.com/Serico14/mycode/master/Red_Fin_Rental_Data_Set_April%20-%20Red_Fin_Rental_Data_Set_April.csv" 
download = requests.get(url).content

# Reading the downloaded content and turning it into a pandas dataframe
df = pd.read_csv(io.StringIO(download.decode('utf-8')))

#Test =  Printing out the first 5 rows of the dataframe
#print (df.head())


