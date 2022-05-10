# Laser and Analysis

We will use a laser perturbation in tune with the lowest energy
transition of the molecule in order to study the photodynamic 
process of absorption in this transition. In order to do this, we
need to know the energy corresponding to the lower energy transition of
the molecule (look for it in the spectrum ploted in the previous calculation)
and calculate the direction of maximal polarization of the transition.  

1) Based on the spectrum calculated previously, calculate the
direction of maximal polarization of the lowest energy transition 
of the molecule. 

- Help: use the tool `calc_timeprop_maxpoldir` already available in
your installation (under: dftbplus/tools/misc/). To know how this 
tool work the user can just type:

    calc_timeprop_maxpoldir -h

- On which/es axis/es have components the obtained vector? Does the result
make sense? Why?
  - Help: try to plot the molecule and see how it is centered with respect
  to the cartesian axes.

2) Prepare the input for the dynamic under a continuos laser perturbation.
Use the energy transition obtained from the spectrum and the vector
obtained above as the direction of the laser. 

  - Why we should use this direction instead of any other?

3) After the dynamic is ended. Take a look at the `mu.dat` file. 
  
  - Is the dipole moment increasing linearly? 

4) Take a look at the `molpopul.dat`
generated. This file contains the populations of the GS orbitals during
the dynamic. 

  - Which orbitals are involved in the transition?
    Help: you can plot the `molpopul.dat` file using xmgrace:
    
    xmgrace -nxy molpopul.dat

    look at the populations at y=2 (occupied orbitals in the GS) and find
    which curves are decreasing during the dynamic. These are the orbitals
    being depopulated.
    look at the populations at y=0 (unoccopied orbitals in the GS) and find
    which curves are increasing during the dynamic. These are the orbitals
    being populated.

5) Let's generate those orbitals using `waveplot`
 
  - Look at the `waveplot_in.hsdi_` template for the input for waveplot:
    - Which files needs this input to run?
    - On which orbitals are we interested?
  - After editing and completing his file, just copy it to `waveplot_in.hsd`and run 
  waveplot using your current installed version that probably is at:

  `$HOME/dftbplus/_build/app/waveplot/waveplot'

  - After running waveplot, a number of files would be generated starting with "wp-1-1"

6) Let's plot those orbitals using VMD:

  - Open the HOMO and LUMO cube files and plot them as an isosurface using the 
  graphical representations options giving by VMD.
  (For a tutorial on the [Basics of VMD](https://www.ks.uiuc.edu/Training/SumSchool/materials/sources/tutorials/01-vmd-tutorial/html/node2.html) and/or the [isosurface](https://www.ks.uiuc.edu/Research/vmd/current/ug/node77.html) method please refer to the links.
