#!/bin/bash

# Usage: ./run_SPPARKS.sh

#   Nsite: # of sites per lattice strip
#    tpts: Total time points for simulation
#      dt: Time interval inbetween each time point
#  Nstrip: # of lattice strips
#    Nsim: # of simulations

Nsite=5
tpts=3000
dt=0.1
Nstrip=100
Nsim=16

# ra2: Rate of adsorption / 2
# rd2: Rate of desorption / 2
# Rates are halfed to account for double counting in simulation
# For example, if ra=1, then ra2 should be provided in SPPARKS
ra2=0.5
rd2=25

spkexe=./spk_nonmui
logdir=../log$Nsite

spkscr=in.diss_ads
sitefilescr=create_site_file.py

# Check spparks executable
if [ ! -f $spkexe ]
then
  echo "ERROR: spparks executable $exec1 not found"
  echo "1. go to ~/GIT/FHDeX/exec/compressible_stag_mui/SPPARKS_MUI"
  echo "2. make nonmui"
  exit
fi

# Check logdir and resdir
if [ -d $logdir ]
then
  echo "ERROR: $logdir already exists"
  exit
fi

# Create logdir 
mkdir $logdir  

# Generate sites data file "data.strips"
python $sitefilescr $Nstrip $Nsite

# Execute spparks then extracts data into res files
# Runs the simulation in group of 16.
for (( i=0; i<$Nsim; i+=16 ))
do
  imax=$(($i + 16<$Nsim ? $i + 16:$Nsim ))

    for seed in $(seq $((i+1)) $imax)
    do
        logfile=$logdir/log${seed}.spparks
        echo "running $spkexe with seed = $seed"
        mpirun -np 1 $spkexe -in $spkscr -log log.spparks$seed -screen none \
          -var seed $seed -var xhi $Nstrip -var yhi $Nsite -var tpts $tpts -var dt $dt -var ra2 $ra2 -var rd2 $rd2 &
        mv $logfile $logdir
    done
    wait
done

# Keep some files for records
cp $spkscr $logdir
mv data.strips $logdir
