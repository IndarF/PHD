#!/bin/bash

# Usage: ./run_plot.sh tpts dt Nsite flag

#   Nsite: # of sites per lattice strip
#    tpts: Total time points for simulation
#      dt: Time interval inbetween each time point
#    flag: 0 if Nsite is outside range [2,8], 1 if within 

Nsite=10
tpts=3000
dt=0.1
flag=0

plotscr=plot.py
statfile=../stat_file$Nsite
rk4file=../rk4_file$Nsite

# Check if data files exist
if [ ! -f $statfile ]
then
  echo "ERROR: statfile doesn't exist"
fi

if [ ! -f $rk4file ]
then
  echo "rk4file doesn't exist, running plot without rk4file"
  python $plotscr $tpts $dt $Nsite $flag
  exit
fi

# Run plot.py
python $plotscr $tpts $dt $Nsite $flag
