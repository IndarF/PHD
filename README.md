This project demonstrates:
1. How to run multiple simulations on SPPARKS with an input script for Dissociative Adsoprtion
2. How to parse the data from simulations to data files
3. Compute mean simulation and RK4 approximation data for Dissociative Adsoprtion
4. Plotting simulation and approximation data to compare equilibrium Surface Coverage

To run this example:
1. copy the executable "spk_nonmui" to the current directory:
   --> cp ~/GIT/FHDeX/exec/compressible_stag_mui/SPPARKS_MUI/spk_nonmui .
2. execute the shell script:
   --> ./diss_ads.sh
   
This project contains the following files:
    README.md            This file
    diss_ads.sh          Main Shell Script
    run_multiple.sh      Shell Script for running Simulations
    in.diss_ads          SPPARKS input script
    create_site_file.py  Creates sites data file "data.strips"
    datagen.py           Creates data file from simulation data
    comp_stat.py         Computes mean and standard error of simulation data
    comp_rk4.py          Computes approximation for Surface Coverage using rk4
    plot.py              Plots simulation and rk4 approximation data
    clean.sh             Deletes all data and outcome files

