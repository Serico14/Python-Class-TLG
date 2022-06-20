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
#static file that requires data manipulation to make standard for dataFrame function

# Reading the downloaded content and turning it into a pandas dataframe
df = pd.read_csv(io.StringIO(download.decode('utf-8')))

#Test =  Printing out the first 5 rows of the dataframe - Success
#print (df.head())

#Unique State Retrieval 
dataFrame = pd.DataFrame(df)
Unique_State = (dataFrame["Region"].unique()) #Pulls State Abbreviation
Unique_State_Count = (len(Unique_State)-1) #Count for all Inputs in Region column (-1 to remove 'National' input)

#National Average Baseline 
NAB= (dataFrame.iat[119,3])
#(dataFrame.query("Region== 'National'")) - Automation attempt, current issue is adding additional filtering to logic for year

#Average Montly Rent by State Mapping
WI = int(dataFrame.iat[0,3]) 
MO = int(dataFrame.iat[5,3])
MN = int(dataFrame.iat[10,3])
RI = int(dataFrame.iat[28,3])
IL = int(dataFrame.iat[37,3])
OH = int(dataFrame.iat[42,3])
MD = int(dataFrame.iat[47,3])
CA = int(dataFrame.iat[52,3])
NC = int(dataFrame.iat[57,3])
DC = int(dataFrame.iat[62,3])
MI = int(dataFrame.iat[96,3])
MA = int(dataFrame.iat[126,3])
CO = int(dataFrame.iat[141,3])
VA = int(dataFrame.iat[146,3])
NV = int(dataFrame.iat[151,3])
IN = int(dataFrame.iat[156,3])
PA = int(dataFrame.iat[166,3])
FL = int(dataFrame.iat[171,3])
GA = int(dataFrame.iat[176,3])
AZ = int(dataFrame.iat[181,3])
TX = int(dataFrame.iat[191,3])
OH = int(dataFrame.iat[201,3])
TN = int(dataFrame.iat[206,3])
NY = int(dataFrame.iat[216,3])
NJ = int(dataFrame.iat[221,3])
WA = int(dataFrame.iat[246,3])
OR = int(dataFrame.iat[256,3])

#Possible automation - create column and row variable based on lookup of state and mapped with python 'iat' function

#Graph Parameters and Details
def main(): 
    R = Unique_State_Count                                                    #Inputs along x axis
    
    Average_Monthly_Rent = (WI,MO,MN,RI,IL,OH,MD,CA,NC,DC,PA,TX,MI,MA,CO,VA,NV,IN,FL,GA,AZ,TN,NY,NJ,WA,OR) #Test
    
    #Average_Monthly_Rent = (20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20) #AMR Test
    #National_Average = (10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10)     #NA Test
    National_Average = (NAB,NAB,NAB,NAB,NAB,NAB,NAB,NAB,NAB,NAB,NAB,NAB,NAB,NAB,NAB,NAB,NAB,NAB,NAB,NAB,NAB,NAB,NAB,NAB,NAB,NAB) 
    #National_Average = for _ in range(Unique_State_Count):
    #    National_Average_Base
    ind = np.arange(R)                                                                                      #Order of Bars 
    width = 11                                                                                               #Width of Bar 
    
    p1 = plt.bar(ind, Average_Monthly_Rent, width)

    p2 = plt.bar(ind, National_Average, width, bottom= Average_Monthly_Rent)
    
    plt.ylabel("Average Monthly Rent (dollars)")
    plt.title("Average Rental Costs by State")
    plt.xticks(ind, ("WI","MO","MN","RI","IL","OH","MD","CA","NC","DC","PA","TX","MI","MA","CO","VA","NV","IN","FL","GA","AZ","TN","NY","NJ","WA","OR"))
    plt.yticks(np.arange(0, 4500, 250))
    plt.legend((p1[0], p2[0]), ("AMR", "NMR"))

    # display the graph
    plt.savefig("/home/student/mycode/FinalProject.png")
    

if __name__ == "__main__":
    main()
