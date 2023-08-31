import matplotlib
import numpy as np
from matplotlib import pyplot as plt
import sys
import re

if len(sys.argv)!=5:
  print("Usage: python %s tpts dt log.spparks res" % sys.argv[0])
  sys.exit()

# Initialize necessary variables for script
tpts = int(sys.argv[1]) + 1                    # Adding 1 to tpts to account for data at t=0
dt = float(sys.argv[2])
infile = sys.argv[3]
outfile = sys.argv[4]
end = tpts*dt
switch1 = 0
switch2 = 0
count = 0

# Reading Input Data File
data_file = open(infile)
lines = data_file.readlines()

# Initializing time step, [X] & [0] arrays using time and delta variables     
x_data = np.zeros(tpts)                        
vac_data = np.zeros(tpts)
t_data = np.arange(0,end, dt)

for line in lines:                                  
    if line.find('Loop time of ') != -1:
        switch1 = 0
        switch2 = 0
    if switch2 == 1:                                # I calculate t using count and dt so that I can determine whether the next line of data 
        t = count*dt                                # is the correct time point. Then, once the line read next contains 'Loop time of ' I turn the switches off
        temp1 = line.split() 
        if temp1[0] == '{}'.format(t):   
            vac_data[count] = int(temp1[-2])       
            x_data[count] = int(temp1[-1])   
            count = count+1 
        if temp1[0] == '{}'.format(int(t)):
            vac_data[count] = int(temp1[-2])       
            x_data[count] = int(temp1[-1])    
            count = count+1       
    if switch1 == 1:                                 # if the count (# of data lines read) is 0, then I read the first line of data. 
        if count == 0:                               # Then switch 2 is turned on
            temp1 = line.split()           
            vac_data[count] = int(temp1[-2])          
            x_data[count] = int(temp1[-1])
            count = count + 1          
            switch2 = 1            
        else:
            switch2 = 1
    if line.find('      Time    Naccept') != -1:      # Once I read the line before the data is listed, I turn switch 1 on.
        switch1 = 1   
data_file.close()

# Generating Output file using t_data, vac_data, x_data
np.savetxt(outfile, np.transpose([t_data, vac_data, x_data]), fmt='%.1f', delimiter='      ', header='Time    Vacant    Occupied')


    
