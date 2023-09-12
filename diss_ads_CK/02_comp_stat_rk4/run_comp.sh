#!/bin/bash

# Usage: ./run_comp.sh Nsite tpts dt ra rd Nstrip Nsim

#   Nsite: # of sites per lattice strip
#    tpts: Total time points for simulation
#      dt: Time interval inbetween each time point
#      ra: Rate of adsorption
#      rd: Rate of desorption
#  Nstrip: # of lattice strips
#    Nsim: # of simulations

Nsite=10
tpts=3000
dt=0.1
ra=1
rd=50
Nstrip=100
Nsim=10      

resdir=../res$Nsite
statscript=comp_stat.py
rk4script=comp_rk4.py
statfile=../stat_file
rk4file=../rk4_file

# Check resdir 
if [ ! -d $resdir ]
then
  echo "ERROR: $resdir doesn't exists"
  exit
fi

# run comp_stat.py
echo Comp_Stat_RK4 run 
python $statscript $Nsite $Nstrip $Nsim $statfile

# Check if Nsite is compatible with rk4 range
if [ $Nsite -gt 1 ] 
then
  if [ $Nsite -lt 9 ]
  then
    echo "This is within range of supported rk4 computations"
    python $rk4script $tpts $dt $Nsite $ra $rd $rk4file
    exit
  fi
fi

