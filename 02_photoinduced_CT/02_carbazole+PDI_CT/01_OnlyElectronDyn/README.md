## Only-Electron Dynamics

1) With the transition dipole moment vector calculated previously, prepare
your input for a laser-driven electron dynamics in tune with the acceptor (PDI)
lowest energy excitation. Use the `dftb_in.hsd_pulse` as a template. Note 
that this time we add an envelope function to the laser perturbation in order
to mimick a laser pulse.

2) After running the electron dynamics, use the provided tool `calc_timeprop_charges.py`
to obtain the total charges per fragment. Try 
	`calc_timeprop_charges.py --help`
to get info about how to use the script. You will have to define the ranges of atoms
that correspond to each of the two molecules.
