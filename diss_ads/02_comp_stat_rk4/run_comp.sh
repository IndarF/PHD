#!/bin/bash

# Usage: ./run_comp Nsite tpts dt ra rd Nstrip Nsim

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
ra=1
rd=50
Nstrip=100
Nsim=10

# rates are halfed to account for double counting in simulation
ra2=$( bc <<<"scale=2; $ra / 2" )
rd2=$( bc <<<"scale=2; $rd / 2" )
# bc used so code can contain the calculation as a float value
# To change # of digits after decimal, change scale value (ex. scale=2 will give you 2 digits after decimal)  

resdir=../res$Nsite
statscript=comp_stat.py
rk4script=comp_rk4.py

# Check resdir 
if [ ! -d $resdir ]
then
  echo "ERROR: $resdir doesn't exists"
  exit
fi

# run comp_stat.py
python $statscript $Nsite $Nstrip $Nsim stat_file

# Check if Nsite is compatible with rk4 range
if [ $Nsite -gt 1 -a $Nsite -lt 9]
then
  echo "This is within range of supported rk4 computations"
  exit
fi











