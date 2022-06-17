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

#Unique State Retrieval 
dataFrame = pd.DataFrame(df)
Unique_State = (dataFrame["Region"].unique()) #Pulls State Abbreviation
Unique_State_Count = (len(Unique_State)) #Count for all Inputs in Region column


#Average Monthly by State

#National Average baseline 
National_Rows = (dataFrame.query("Region== 'National'"))  #"Month== 'April_2022'"))

# Attempt to pull out April 2022 National Rent Prices for baseline against all other information

#print(National_Rows)


def main(): 
    R = Unique_State_Count                                                    #Inputs along x axis
    #Average_Monthly_Rent = (20,30,40,50)                  #Bar 1 Actual - How to properly map this so that (for example:Texas data is populated for Bar                                                                      dedicated to Texas and not some other region? 
    Average_Monthly_Rent = (20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20) #Test
    National_Average = (10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10) #Test2
    
    #National_Average = (10, 10, 10, 10)                      #Bar 2 - Actual
    ind = np.arange(R)                                       #Order of Bars 
    width = 4                                             #Width of Bar 
    
    p1 = plt.bar(ind, Average_Monthly_Rent, width)

    p2 = plt.bar(ind, National_Average, width, bottom= Average_Monthly_Rent)
    
    plt.ylabel("Average Monthly Rent (dollars)")
    plt.title("Average Rental Costs by State")
   # plt.xticks(ind, ("1","2","3","4"))
    plt.xticks(ind, ("WI","MO","MN","National","RI","IL","OH","MD","CA","NC","DC","PA","TX","MI","MA","CO","VA","NV","IN","FL","GA","AZ","TN","NY","NJ","WA","OR"))
    plt.yticks(np.arange(0, 81, 10))
    plt.legend((p1[0], p2[0]), ("AMR", "NMR"))

    # display the graph
    plt.savefig("/home/student/mycode/FinalProject.png")
    

if __name__ == "__main__":
    main()
