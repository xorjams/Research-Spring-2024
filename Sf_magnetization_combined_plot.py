# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 18:31:24 2023

@author: 15083
"""

import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
color = iter(cm.rainbow(np.linspace(0, 1, 10)))
test = 0
fig, ax = plt.subplots()
ax.set_ylabel("Magnetization")
ax.set_xlabel("Temperature")
#for i in [4.5,4,3.5,3,2.5,2, 1.5,1,0.5,0]:
    
os.chdir('C:\\Users\\15083\\Documents\\NEU_semester_2\\Feiguin_Group_Research_Spring_2022\\Code\\4x4x4_neg1mu_neg0.5Dope_Dope0_trial4')

filenames =  os.listdir('C:\\Users\\15083\\Documents\\NEU_semester_2\\Feiguin_Group_Research_Spring_2022\\Code\\4x4x4_neg1mu_neg0.5Dope_Dope0_trial4')


def read_col1(fname, col=0, convert=float, sep=None):

    with open(fname) as fobj:
         return [convert(line.split(sep=sep)[col]) for line in fobj]
     
        
     
def read_col2(fname, col = 1, convert = float, sep=None):
    with open(fname) as fobj:
         return [convert(line.split(sep=sep)[col]) for line in fobj]

     
def read_col3(fname, col = 2, convert = float, sep=None):
    with open(fname) as fobj:
         return [convert(line.split(sep=sep)[col]) for line in fobj]

     
        

Data1 = np.loadtxt("Dope1")  
#sfStaggMag = Data1[:,2]
sfTemp = Data1[:,0]
sfMag = Data1[:,1]

DataCombine = np.column_stack((sfTemp, sfMag))

DataCombineSort =  DataCombine[np.argsort(DataCombine[:, 0])]

sfTemp = DataCombineSort[:,0]
sfMag = DataCombineSort[:,1]



    

#sfTemp.sort()
#sfEnergy.sort()

sfTemp = np.asarray(sfTemp)

sfTempSD = np.std(sfTemp)

#sfStaggMagSD = np.std(sfStaggMag)

sfTempError = sfTempSD/np.sqrt(1000)


#sfStaggError = sfStaggMagSD/np.sqrt(1000)

   




#for i in [4.5,4,3.5,3,2.5,2, 1.5,1,0.5,0]:
    
os.chdir('C:\\Users\\15083\\Documents\\NEU_semester_2\\Feiguin_Group_Research_Spring_2022\\Code\\4x4x4_neg1mu_neg0.5Dope_Dope10_trial4')

filenames =  os.listdir('C:\\Users\\15083\\Documents\\NEU_semester_2\\Feiguin_Group_Research_Spring_2022\\Code\\4x4x4_neg1mu_neg0.5Dope_Dope10_trial4')


def read_col1(fname, col=0, convert=float, sep=None):

    with open(fname) as fobj:
         return [convert(line.split(sep=sep)[col]) for line in fobj]
     
        
     
def read_col2(fname, col = 1, convert = float, sep=None):
    with open(fname) as fobj:
         return [convert(line.split(sep=sep)[col]) for line in fobj]

     
def read_col3(fname, col = 2, convert = float, sep=None):
    with open(fname) as fobj:
         return [convert(line.split(sep=sep)[col]) for line in fobj]

     
        

Data2 = np.loadtxt("Dope1") 
Data2[:,1] 
sfTemp2 =  Data2[:,0]
sfMag2 =  Data2[:,1]
#sfStaggMag = Data1[:,2]


DataCombine = np.column_stack((sfTemp2, sfMag2))

DataCombineSort =  DataCombine[np.argsort(DataCombine[:, 0])]

sfTemp2 = DataCombineSort[:,0]
sfMag2 = DataCombineSort[:,1]






#os.chdir('C:\\Users\\15083\\Documents\\NEU_semester_2\\Feiguin_Group_Research_Spring_2022\\Code\\6x6_neg6Dope_magDope10_Dope1')

#Data = np.loadtxt("L_20_datatest.txt")  


#Temp = Data[:,0]
#StaggMag = Data[:,3]


#sfTempcorrect = Temp
#sfStaggMagcorrect = StaggMag

#TempError = np.std(Temp)/np.sqrt(1000)
#MagError = np.std(sfMag)/np.sqrt(1000)


plt.plot(sfTemp,sfMag, marker = ".", label = "Dope0")
plt.plot(sfTemp2,sfMag2, marker = ".", label = "Dope10")
#plt.errorbar(sfTempcorrect, sfStaggMagcorrect, yerr = StaggMagError, marker = ".")
c = next(color)
#plt.plot(sfTemp, sfMag, c=c, marker = ".", label = "\u03BC = " + str(-i))
#plt.plot(sfTemp2, sfMag2, marker = ".", label = "Dope4")
#plt.xscale("Log")
plt.legend(loc="upper right")
plt.title("4x4x4  \u03BC = -1 DL = -0.5 Dope0 and 10 trial 4")



plt.show()