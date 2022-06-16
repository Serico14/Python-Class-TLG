#!/usr/bin/env python3
import os

# Libraries needed for the tutorial
import pandas as pd
import requests
import io
import numpy as np
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

# Downloading the csv file from your GitHub account
url = "https://raw.githubusercontent.com/Serico14/mycode/master/Red_Fin_Rental_Data_Set_April%20-%20Red_Fin_Rental_Data_Set_April.csv" 
download = requests.get(url).content

# Reading the downloaded content and turning it into a pandas dataframe
df = pd.read_csv(io.StringIO(download.decode('utf-8')))

#Test =  Printing out the first 5 rows of the dataframe
#print (df.head())

def main(): 
    R = 4
    Average_Monthly_Rent = (20, 35, 30, 35)
    National_Average = (25, 32, 34, 20)
    ind = np.arange(R)
    width = 0.45
    
    p1 = plt.bar(ind, Average_Monthly_Rent, width)

    p2 = plt.bar(ind, National_Average, width, bottom= Average_Monthly_Rent)
    
    plt.ylabel("Average Monthly Rent (dollars)")
    plt.title("Average Rental Costs by State")
    plt.xticks(ind, ("Q1", "Q2", "Q3", "Q4"))
    plt.yticks(np.arange(0, 81, 10))
    plt.legend((p1[0], p2[0]), ("AMR", "NMR"))

    # display the graph
    # plt.show() # you can try this on a Python IDE with a GUI if you'd like
    plt.savefig("/home/student/mycode/FinalProject.png")
    
if __name__ == "__main__":
    main()
