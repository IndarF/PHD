This project demonstrates:
1. How to run multiple simulations on SPPARKS with an input script for Dissociative Adsoprtion
2. How to parse the data from simulations to data files
3. Compute mean simulation and rk4 approximation data for Dissociative Adsoprtion
4. Plotting simulation and approximation data to compare equilibrium Surface Coverage

To run this example:
1. copy the executable "spk_nonmui" to '01_run_diss_ads':
   --> cp ~/GIT/FHDeX/exec/compressible_stag_mui/SPPARKS_MUI/spk_nonmui 01_run_diss_ads
2. execute the shell script in '01_run_diss_ads':
   --> ./run_multiple.sh
3. execute the shell script in '02_comp_stat_rk4':
   --> ./run_comp.sh
4. execute the shell script in '03_plot_data':
   --> ./run_plot.sh
   
This project contains the following files:
    README.md            This file
    run_multiple.sh      Shell Script for running Simulations
    in.diss_ads          SPPARKS input script
    create_site_file.py  Creates sites data file "data.strips"
    datagen.py           Creates data file from simulation data
    run_comp.sh          Shell Script for generating mean simulation and rk4 data
    comp_stat.py         Computes mean and standard error of simulation data
    comp_rk4.py          Computes approximation for Surface Coverage using rk4
    run_plot.sh          Shell Script for plotting data
    plot.py              Plots simulation and rk4 approximation data
    clean.sh             Deletes all data and outcome files

