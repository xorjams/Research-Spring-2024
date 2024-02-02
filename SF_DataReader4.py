# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 19:50:58 2022

@author: 15083
"""


import numpy as np
import os
import shutil
import pandas as pd

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]
os.chdir('C:\\Users\\15083\\Documents\\NEU_semester_2\\Feiguin_Group_Research_Spring_2022\\Code\\4x4x4_neg1mu_neg0.5Dope_Dope10_trial4')

filenames =  os.listdir('C:\\Users\\15083\\Documents\\NEU_semester_2\\Feiguin_Group_Research_Spring_2022\\Code\\4x4x4_neg1mu_neg0.5Dope_Dope10_trial4')
'''
def read_col(fname, col=0, convert=float, sep=None):

    with open(fname) as fobj:
         return [convert(line.split(sep=sep)[col]) for line in fobj]

def read_col2(fname, col=1, convert=float, sep=None):

    with open(fname) as fobj:
         return [convert(line.split(sep=sep)[col]) for line in fobj]
   
def read_col3(fname, col=2, convert=float, sep=None):

    with open(fname) as fobj:
         return [convert(line.split(sep=sep)[col]) for line in fobj]


def read_col4(fname, col=3, convert=float, sep=None):

    with open(fname) as fobj:
         return [convert(line.split(sep=sep)[col]) for line in fobj]

'''

filenameslen = len(filenames)

f = open("Dope1", "w")
for i in range(filenameslen):
    columns = max((len(l.split()) for l in open(str(filenames[i]))), default = 0)
    
    df = pd.read_table(str(filenames[i]), 
                       delim_whitespace=True, 
                       header=None, 
                       usecols=range(columns), 
                       engine='python')
    
    
    Data = np.array(df)
    currentname = filenames[i]
    currentnameparts = currentname.split('_')
    Temp = currentnameparts[2]
    mu = currentnameparts[5]
    Temp = float(Temp)
    mu = float(mu)

    res2 = Data[:,1]

    

    MagnetizationArray = np.asarray(res2)

    
    Beta = 1/Temp

    #HeatCapacity = np.average(HeatCapacityArray)

    #HeatCapacityArray -= AvgEnergy**2
    #HeatCapacity = (Beta**2)*np.average(HeatCapacityArray)

    Magnetization = np.average(MagnetizationArray)
   



    
   # AvgHeatCap = np.average(HeatCapacityArray)/(Temp*Temp)
    
    #AvgHeatCap = (AvgEnergySquare - AvgEnergy**2)/(Temp**2)
    #Temp = round(Temp, 0)
    

    print(Temp)
    print(mu)
    
    f.write('{:<12}  {:<12} '.format(Temp,  Magnetization))
    f.write("\n")

            
            
f.close()