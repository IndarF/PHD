#!/bin/bash

# Usage: ./run_multiple Nsite tpts dt ra rd Nstrip Nsim

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

spkexe=./spk_nonmui
logdir=../log$Nsite
resdir=../res$Nsite

spkscr=in.diss_ads
sitefilescr=create_site_file.py
datagenscr=datagen.py

# check spparks executable
if [ ! -f $spkexe ]
then
  echo "ERROR: spparks executable $exec1 not found"
  echo "1. go to ~/GIT/FHDeX/exec/compressible_stag_mui/SPPARKS_MUI"
  echo "2. make nonmui"
  exit
fi

# check logdir and resdir
if [ -d $logdir ]
then
  echo "ERROR: $logdir already exists"
  exit
fi
if [ -d $resdir ]
then
  echo "ERROR: $resdir already exists"
  exit
fi

# create logdir and resdir
mkdir $logdir $resdir 

# generate sites data file "data.strips"
python $sitefilescr $Nstrip $Nsite

# execute spparks then extracts data into res files
for ((i = 1 ; i <= $Nsim ; i++)); do
  echo ** SPPARKS run $i
  mpirun -np 1 $spkexe -in $spkscr -log log.spparks$i -screen none \
    -var seed $i -var xhi $Nstrip -var yhi $Nsite -var tpts $tpts -var dt $dt -var ra $ra2 -var rd $rd2
  mv log.spparks$i $logdir 
  python $datagenscr $tpts $dt $logdir/log.spparks$i $resdir/res$i  
done

# keep some files for records
cp $spkscr $logdir
mv data.strips $logdir
