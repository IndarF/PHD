import matplotlib
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors as mcolors
import sys

if len(sys.argv)!=5:
  print("Usage: python %s tpts dt Nsite flag" % sys.argv[0])
  sys.exit()

# Initialize necessary variables for script
tpts = int(sys.argv[1])
dt = float(sys.argv[2])
Nsite = int(sys.argv[3])
flag = int(sys.argv[4])
time = float(tpts*dt)

# Checking flag value for rk4 inclusion
if flag==1:
    stat_time = np.loadtxt('../stat_file{}'.format(Nsite), usecols = 0)
    rk4_time = np.loadtxt('../rk4_file{}'.format(Nsite), usecols = 0)  
    stat_data = np.loadtxt('../stat_file{}'.format(Nsite), usecols = 1)
    rk4_data = np.loadtxt('../rk4_file{}'.format(Nsite), usecols = 1)  
    plt.figure(1)
    plt.plot(stat_time, stat_data, color="blue", label='N={}'.format(Nsite), alpha = 0.25)
    plt.plot(rk4_time, rk4_data, 'k-', label='RK4')
    plt.axis([-5, time, 0, rk4_data[tpts]+0.1 ])
    plt.xlabel('Time')
    plt.ylabel('Coverage')
    plt.legend(loc='upper right', ncol=2)
    plt.title('Surface Coverage for Dissociative Adsorption')
    plt.savefig("../scrk4.png")
else:
    stat_time = np.loadtxt('../stat_file{}'.format(Nsite), usecols = 0) 
    stat_data = np.loadtxt('../stat_file{}'.format(Nsite), usecols = 1)
    plt.figure(1)
    plt.plot(stat_time, stat_data, color="blue", label='N={}'.format(Nsite), alpha = 0.25)
    plt.axis([-5, time, 0, stat_data[tpts]+0.1 ])
    plt.xlabel('Time')
    plt.ylabel('Coverage')
    plt.legend(loc='upper right', ncol=2)
    plt.title('Surface Coverage for Dissociative Adsorption')
    plt.savefig("../scrk4.png")









