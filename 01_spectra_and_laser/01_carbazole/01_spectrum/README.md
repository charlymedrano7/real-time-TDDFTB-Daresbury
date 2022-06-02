## We will calculate the absorption spectrum of carbazole using
## real-time TDDFTB

1) Take a look at the input coordinates `coords.gen`. The .gen format
is the one used for DFTB+ code. In order to visualize the molecule,
you can use the "gen2xyz" script, provided in the installation of the 
DFTB+ code, doing:

  gen2xyz coords.gen

This will generate a coords.xyz that you can open with VMD, Avogadro or
any other molecular visualization software of your choice.

2) Open the "dftb_in.hsd_spec" file. This is a template for the calculation
of the absorption spectrum.

  - Take a look at the ElectronDynamics block at the end of the file.
  - The input variables to be considered for the calculation of the spectrum are four:
    	a) Steps (integer): the number of steps of the dynamics. It defines the time window and, consequently, the energy window of the spectrum. The longer the dynamic, the lower the energies that can be reached in the spectrum are (also afected by the timestep, of course). Here, we will use 10000 steps.
       b) TimeStep (float): the time step in time units. Usually 0.2 a.u (0.0048 fs). It defines the resolution of the spectrum. The smaller the time step, the higher the resolution within the time window.
    	c) Perturbation: In this case we need a kick perturbation (Dirac delta) and we need to specify the PolarizationDirection that could be "X", "Y", "Z" (if we are interested in one particular direction) or "all" if we want to calculate the whole absorption spectrum. Set it as "all".
    	d) FieldStrength (float): the field strength of the perturbation applied. For the calculation of the absorption spectrum, it must be within the linear response regime, i.e. usually 0.001 V/AA.
  - Complete the template file, copy it to "dftb_in.hsd" and run the calculation.

3) Once the dynamics ended, we will have 3 components of the dynamical dipole moment ("mux.dat", "muy.dat", "muz.dat"). We need to Fourier-transform these dipole components in order to obtain the absorption spectrum of the molecule. To do this, we will use the tool `calc_timeprop_spec` available after installation of DFTB+ under: "dftbplus/tools/misc/calc_timeprop_spectrum". In the folder
where you have the dipole files just type:

  calc_timeprop_spectrum -d 4 -f 0.001

the option -d is for the damping constant (in fs) applied to the dipole moment before transformation.
The option -f stands for the field strength (in V/AA) of the perturbation applied during dynamic.

4) After running the script you will find two new files: "spec-nm.dat" and "spec-ev.dat" which are the absorption spectra in nm and eV, respectively. Plot the spectrum file with the plotting tool of your desire and look at the lower energy transitions.

5) Change the damping constant for a higher value, recalculate the specctrum and plot both spectra together. Which is the effect of the damping time in the spectrum?
