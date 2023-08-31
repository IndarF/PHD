#!/bin/bash

# Usage: ./plot_gen.sh
#    tpts: Total time points for simulation
#      dt: Time interval inbetween each time point
#      ra: Rate of Adsorption
#      rd: Rate of Desorption
#    Nmin: Minimum size of lattice strip (Must be >= 2)
#    Nmax: Maximum size of lattice strip (must be <= 8)
#  Nstrip: # of lattice strips 
#    Nsim: # of simulations per strip size

# Taking in all parameters inputted
Nmin=2
Nmax=8
Nstrip=100
Nsim=100
ra=1
rd=50
tpts=3000
dt=0.1

# Run simulations for each lattice length, then generate data files from simulations and rk4 approximations
for ((i = $Nmin ; i <= $Nmax ; i++)); do
  ./01_run_diss_ads/run_multiple.sh $i $tpts $dt $ra $rd $Nstrip $Nsim
  python 02_comp_stat_rk4/comp_stat.py $i $Nstrip $Nsim stat_file
  python 02_comp_stat_rk4/comp_rk4.py $tpts $dt $i $ra $rd rk4_file
done

# Generate even and odd Surface Coverage Plots
python 03_plot_data/plot.py $tpts $dt $Nmin $Nmax
