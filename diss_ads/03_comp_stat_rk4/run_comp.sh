#!/bin/bash

# Usage: ./run_comp.sh 

#   Nsite: # of sites per lattice strip
#    tpts: Total time points for simulation
#      dt: Time interval inbetween each time point
#      ra: Rate of adsorption
#      rd: Rate of desorption
#  Nstrip: # of lattice strips
#    Nsim: # of simulations

Nsite=5
tpts=3000
dt=0.1

# Use the whole value of the rates for rk4 approximations
ra=1
rd=50

Nstrip=100
Nsim=16      

resdir=../res$Nsite
statscript=comp_stat.py
rk4script=comp_rk4.py
statfile=../res$Nsite/stat_file
rk4file=../res$Nsite/rk4_file

# Check resdir 
if [ ! -d $resdir ]
then
  echo "ERROR: $resdir doesn't exists"
  exit
fi

# Run comp_stat.py and comp_rk4.py
echo Comp_Stat_RK4 run 
python $statscript $Nsite $Nstrip $Nsim $statfile
python $rk4script $tpts $dt $Nsite $ra $rd $rk4file