## Ehrenfest Dynamics

1) With the transition dipole moment vector calculated previously, prepare
your input for a Laser electron dynamics in tune with the acceptor (PDI)
lower energy excitation. Use the `dftb_in.hsd_Ehrenfest` as a template. Note 
that this time we add an envelope shape to the laser perturbation in order
to mimik a laser pulse.

Now we will allow the ions to move within the Ehrenfest approach using:

IonDynamics = Yes
InitialTemperature [k] = 0

in the ElectronDynamics block. The first flag just tell the ions to move 
during the dynamic and the second one just set the T at t=0 of the dynamic.
If the last is set to a T not equal to 0, the ions will start the dynamic
with a velocity distribution corresponding to the Maxwell-Boltzmann
distribution at that temperature. One can also add the velocities obtained
from a previous run using the flag Velocities instead of InitialTemperature 
(see manual page 85, section 2.8 ElectronDynamics).

2) After running the electron dynamic, use the provided tool `charges.py`
to obtain the total charges per fragment. Try:
	calc_timeprop_charges.py --help
to get info about how to use the script

3) Plot the charge vs time for each fragment and compare them with the ones
obtained in the only-electron Dynamic.

4) Take a look at the tdcoods.xyz file. This file contains the positions (x,y,z)
in angstrom and the velocities (v_x, v_y, v_z) in angstrom/ps. If you open this
file with VMD you will have a nice movie of the nuclear movement during the
dynamic.
