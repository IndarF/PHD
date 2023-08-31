import matplotlib
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors as mcolors
import sys
import re

if len(sys.argv)!=5:
  print("Usage: python %s tpts dt Nmin Nmax" % sys.argv[0])
  sys.exit()

# Initialize necessary variables for script
tpts = int(sys.argv[1])
dt = float(sys.argv[2])
Nmin = int(sys.argv[3])
Nmax = int(sys.argv[4])
time = float(tpts*dt)
countodd = 0
counteven = 0

# Checking if user inputted values wrong
if Nmin > Nmax:
    print("Error, Nmin is greater than Nmax, please make sure Nmin < Nmax")
    sys.exit()

# Initializing arrays data files based on Nmin and Nmax
if Nmin == Nmax:
    stat_time = np.loadtxt('stat_file{}'.format(Nmin), usecols = 0)      # If Nmin == Nmax, then the code just plots the simulation and rk4 data on the lattice 
    rk4_time = np.loadtxt('rk4_file{}'.format(Nmin), usecols = 0)  
    stat_data = np.loadtxt('stat_file{}'.format(Nmin), usecols = 1)
    rk4_data = np.loadtxt('rk4_file{}'.format(Nmin), usecols = 1)  
    
    plt.figure(1)
    plt.plot(stat_time, stat_data, color="blue", label='N={}'.format(Nmin), alpha = 0.25)
    plt.plot(rk4_time, rk4_data, 'k-', label='RK4')
    plt.axis([-5, time, 0, rk4_data[tpts]+0.1 ])
    plt.xlabel('Time')
    plt.ylabel('Coverage')
    plt.legend(loc='upper right', ncol=2)
    plt.title('Surface Coverage for Dissociative Adsorption')
    plt.savefig("scrk4.png")
else: 
    # Take in initial time points from minimum lattice length
    
    stat_time = np.loadtxt('stat_file{}'.format(Nmin), usecols = 0)
    rk4_time = np.loadtxt('rk4_file{}'.format(Nmin), usecols = 0)
    
    # make array of SC and RK4 data based on Nmin and Nmax, and sort data by even and odd lattice lengths
    
    N = range(Nmin, Nmax+1)
    
    for i in N:
        if i % 2 == 0:
            counteven = counteven + 1
        else:
            countodd = countodd + 1
            
    stat_odd = np.zeros((len(stat_time), countodd))
    stat_even = np.zeros((len(stat_time), counteven))
    rk4_odd = np.zeros((len(rk4_time), countodd))
    rk4_even = np.zeros((len(rk4_time), counteven))
    
    # reading surface coverage data
    for i in range(1, counteven+1):
        stat_even[:,i-1] = np.loadtxt('stat_file{}'.format(2*i), usecols = 1)
        rk4_even[:,i-1] = np.loadtxt('rk4_file{}'.format(2*i), usecols = 1) 
    for i in range(1, countodd+1):
        stat_odd[:,i-1] = np.loadtxt('stat_file{}'.format(2*i + 1), usecols = 1)
        rk4_odd[:,i-1] = np.loadtxt('rk4_file{}'.format(2*i + 1), usecols = 1) 
    
    # plotting odd and even lattice lengths
    plt.figure(1)
    for i in range(1, countodd+1):
        plt.plot(stat_time, stat_odd[:,i-1], label='N={}'.format(2*i +1), alpha = 0.5)
    for i in range(1, countodd+1):
        plt.plot(rk4_time, rk4_odd[:,i-1], 'k-', label='RK4')   
    plt.axis([-5, time, 0, rk4_odd[tpts ,countodd-1] + 0.1])
    plt.xlabel('Time')
    plt.ylabel('Coverage')
    plt.legend(loc='upper right', ncol=2)
    plt.title('Surface Coverage for Dissociative Adsorption')
    plt.savefig('scrk4_odd.png')
    
    plt.figure(2)
    for i in range(1, counteven+1):
        plt.plot(stat_time, stat_even[:,i-1], label='N={}'.format(2*i), alpha = 0.5)
    for i in range(1, counteven+1):
        plt.plot(rk4_time, rk4_even[:,i-1], 'k-', label='RK4')   
    plt.axis([-5, time, 0, rk4_even[tpts ,counteven-1] + 0.1])
    plt.xlabel('Time')
    plt.ylabel('Coverage')
    plt.legend(loc='upper right', ncol=2)
    plt.title('Surface Coverage for Dissociative Adsorption')
    plt.savefig('scrk4_even.png')

sys.exit()











