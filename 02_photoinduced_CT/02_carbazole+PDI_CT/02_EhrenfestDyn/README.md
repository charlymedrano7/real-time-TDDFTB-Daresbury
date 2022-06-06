## Electron-Ion (Ehrenfest) Dynamics

1) Again, consider a laser-driven dynamics in tune with the acceptor (PDI)
lowest energy excitation, using a pulse (i.e. including an envelope function). 
Use the `dftb_in.hsd_Ehrenfest` as a template. 
Now we will allow the ions to move within the Ehrenfest approach using:

IonDynamics = Yes
InitialTemperature [k] = 0

in the ElectronDynamics block. The first flag just tells the ions to move 
during the dynamics and the second one just set the temperature at t=0 of the dynamics.
If the last is set to a T not equal to 0, the ions will start the dynamic
with a velocity distribution corresponding to a random sampling from a Maxwell-Boltzmann
distribution at that temperature. One can also set the velocities of all the atoms obtained
from a previous run using the flag Velocities instead of InitialTemperature 
(see DFTB+ Manual, page 85, section 2.8 ElectronDynamics).

2) After running the electron dynamic, use the provided tool `calc_timeprop_charges.py`
to get the net charges per fragment.

3) Plot the net charge vs. time for each fragment and compare them with the ones
obtained in the electron-only dynamics.

4) Take a look at the tdcoods.xyz file. This file contains the positions (x,y,z)
in AA, followed by the velocities (vx, vy, vz) in AA/ps. If you open this
file with a visualization tool you will have a nice movie of the nuclear motion induced 
by the laser the dynamics. Keep in mind that the Ehrenfest approximation does not reproduce
correctly the electron-ion coupling, hence use these results with care.
