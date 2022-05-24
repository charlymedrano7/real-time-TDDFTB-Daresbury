## Only-Electron Dynamics

1) With the transition dipole moment vector calculated previously, prepare
your input for a Laser electron dynamics in tune with the acceptor (PDI)
lower energy excitation. Use the `dftb_in.hsd_pulse` as a template. Note 
that this time we add an envelope shape to the laser perturbation in order
to mimik a laser pulse.

2) After running the electron dynamic, use the provided tool `charges.py`
to obtain the total charges per fragment. Try 
	calc_timeprop_charges.py --help
to get info about how to use the script
