#!/bin/bash

# Usage: ./run_parse.sh

#   Nsite: # of sites per lattice strip
#    tpts: Total time points for simulation
#      dt: Time interval inbetween each time point
#    Nsim: # of simulations

Nsite=5
tpts=3000
dt=0.1
Nsim=16

logdir=../log$Nsite
resdir=../res$Nsite

datagenscr=datagen.py

# Check if log exists and if res doesn't exist
if [ ! -d $logdir ]
then
  echo "ERROR: $logdir doesn't exists"
  exit
fi

if [ -d $resdir ]
then
  echo "ERROR: $resdir already exists"
  exit
fi

# Create res directory
mkdir $resdir

# Parse data from log files
for ((i = 1 ; i <= $Nsim ; i++))
do
  python $datagenscr $tpts $dt $logdir/log.spparks$i $resdir/res$i
done

echo "Log files have been parsed"