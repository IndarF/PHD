#!/bin/bash

# Usage: ./run_multiple Nsite tpts dt ra rd Nstrip Nsim
#   Nsite: # of sites per lattice strip
#    tpts: Total time points for simulation
#      dt: Time interval inbetween each time point
#      ra: Rate of Adsorption
#      rd: Rate of Desorption
#  Nstrip: # of lattice strips 
#    Nsim: # of simulations per strip size
spkexe=./spk_nonmui
spkscr=01_run_diss_ads/in.diss_ads
tpts=$2
dt=$3
start=1
end=$7
xhi=$6
yhi=$1
ra=$( bc <<<"scale=2; $4 / 2" )    # bc used so code can contain the calculation as a float value
rd=$( bc <<<"scale=2; $5 / 2" )    # rates are halfed to account for double counting in simulation
                                   # To change # of digits after decimal, change scale value (ex. scale=2 will give you 2 digits after decimal)  
# spparks executable
if [ ! -f $spkexe ]
then
  echo "ERROR: spparks executable $exec1 not found"
  echo "1. go to ~/GIT/FHDeX/exec/compressible_stag_mui/SPPARKS_MUI"
  echo "2. make nonmui"
  exit
fi

# Generate Directories for data
mkdir res$yhi  log$yhi

# generate sites data file "data.strips"
python 01_run_diss_ads/create_site_file.py $xhi $yhi

# execute spparks then extracts data into res files
for ((i = $start ; i <= $end ; i++)); do
  mpirun -np 1 $spkexe -in $spkscr -log log.spparks$i -var seed $i -var xhi $xhi -var yhi $yhi -var tpts $tpts -var dt $dt -var ra $ra -var rd $rd
  mv log.spparks$i log$yhi
  python 01_run_diss_ads/datagen.py $tpts $dt log$yhi/log.spparks$i res$yhi/res$i  
done
echo "** spparks run completed"
