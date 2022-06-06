# Laser and Analysis

We will consider a laser perturbation in tune with the lowest energy
transition of the molecule in order to study the photodynamic 
process of absorption in this transition. In order to do this, we
need to know the energy of the lowest energy transition of
the molecule (look for it in the spectrum plotted in the previous calculation)
and calculate the direction of maximal polarization of the transition.  

1) Based on the spectrum calculated previously, calculate the
direction of maximal polarization of the lowest energy transition 
of the molecule. 

- Help: use the tool `calc_timeprop_maxpoldir` already available in
your installation (under: dftbplus/tools/misc/). To know how this 
tool work the user can just type:

    `calc_timeprop_maxpoldir -h`

- Along which axes is the direction vector? How is this explained?
  - Hint: try to visualize the molecule and see how it is oriented with respect
  to the cartesian axes.

2) Prepare the input for the dynamics under a continuous laser perturbation.
Use the energy transition obtained from the spectrum as the laser energy and the vector obtained above as the direction of the laser.

  - Why we should use this direction instead of any other?

3) After the dynamics, take a look at the `mu.dat` file. 
  
  - Is the dipole moment increasing linearly? 

4) Take a look at the `molpopul.dat`
generated. This file contains the populations projected on the GS orbitals during the dynamics. 

  - Which orbitals are involved in the transition?
    Help: you can plot the `molpopul.dat` file using xmgrace:
    
    `xmgrace -nxy molpopul.dat`

    Look at the populations at y=2 (occupied orbitals in the GS basis) and find
    which curves are decreasing during the dynamic. These are the orbitals
    being depopulated.
    Look at the populations at y=0 (unoccopied orbitals in the GS basis) and find
    which curves are increasing during the dynamics. These are the orbitals
    being populated.

5) Let's generate those orbitals using `waveplot`
 
  - Look at the `waveplot_in.hsd_` template input file for waveplot:
    - Which files are needed?
    - In which orbitals are we interested?
  - After editing and completing this file, just rename it to `waveplot_in.hsd` and run 
  waveplot using your current installed version that probably is at:

  `$HOME/dftbplus/_build/app/waveplot/waveplot'

  - After running waveplot, a number of files would be generated starting with "wp-1-1".

6) Let's plot these orbitals:

  - Open the cube files that correspond to the HOMO and LUMO and plot them as an isosurface.
  
  (For a tutorial on the [Basics of VMD](https://www.ks.uiuc.edu/Training/SumSchool/materials/sources/tutorials/01-vmd-tutorial/html/node2.html) and/or plotting an [isosurface](https://www.ks.uiuc.edu/Research/vmd/current/ug/node77.html) method please refer to the links.)
