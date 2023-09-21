#!/bin/bash

# Usage: ./run_multiple.sh

#   Nsite: # of sites per lattice strip
#    tpts: Total time points for simulation
#      dt: Time interval inbetween each time point
#  Nstrip: # of lattice strips
#    Nsim: # of simulations

Nsite=10
tpts=3000
dt=0.1
Nstrip=100
Nsim=10

# ra2: Rate of adsorption / 2
# rd2: Rate of desorption / 2
# rates are halfed to account for double counting in simulation
# for example, if ra=1, then ra2 should be provided in SPPARKS
ra2=0.5
rd2=25

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
for ((i = 1 ; i <= $Nsim ; i++))
do
  echo "** SPPARKS run $i"
  mpirun -np 1 $spkexe -in $spkscr -log log.spparks$i -screen none \
    -var seed $i -var xhi $Nstrip -var yhi $Nsite -var tpts $tpts -var dt $dt -var ra2 $ra2 -var rd2 $rd2
  mv log.spparks$i $logdir 
  python $datagenscr $tpts $dt $logdir/log.spparks$i $resdir/res$i  
done

# keep some files for records
cp $spkscr $logdir
mv data.strips $logdir
