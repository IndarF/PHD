#!/bin/bash

# Usage: ./run_plot.sh tpts dt Nsite flag

#   Nsite: # of sites per lattice strip
#    tpts: Total time points for simulation
#      dt: Time interval inbetween each time point
#    flag: 0 if Nsite is outside range [2,8], 1 if within 

Nsite=5
tpts=3000
dt=0.1
flag=1

plotscr=plot.py
statfile=../res$Nsite/stat_file$Nsite
plotdir=../plots

# Check if Stat file exist
if [ ! -f $statfile ]
then
  echo "ERROR: statfile doesn't exist"
fi

# Make directory for plots
mkdir $plotdir

# Run plot.py
python $plotscr $tpts $dt $Nsite $flag    # Script uses flag to determine whether to include rk4 approximation in plot or not
