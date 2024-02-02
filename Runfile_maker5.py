# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 20:10:01 2023

@author: 15083
"""

import numpy as np
from math import floor
from math import log10

def find_exp(number) -> int:
    base10 = log10(abs(number))
    return abs(floor(base10))

L_list = [20]
beta_list = np.hstack([np.arange(0.1,1,0.1),np.arange(1.0,10.0,1.0),np.arange(10.0,101.0,10.0),np.arange(100.0,1001.0,100.0)])
#T_list = np.arange(0.01, 0.4, 0.01)
T_list = np.arange(0.005,0.2,0.01)
Step_list = np.hstack([[2],[20], [200]])
mu_list = [-5,-4.8,-4.6]
D_list = np.arange(0.1,5,0.1)

D_list = np.around(D_list, decimals = 1)

Dict_format = " -c  -1 -d  3 -s 4  -SW  50 -ST 2 -ME  10000 -T {T:.14e} -u -2 -Imp 4 -sp 5 -LV 1 \n" #ME 20000 default


with open("test_run7.txt","w") as IO:
    
    for T in T_list: #for LV in D_list:

        
     
        
        IO.write(Dict_format.format(T=T)) #M=M
            
                
            