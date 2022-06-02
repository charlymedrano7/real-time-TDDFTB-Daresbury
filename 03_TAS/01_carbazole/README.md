# Instructions

1. Take a look at the input dftb_in.hsd_pump. This input is essentially
the same as in case of a pulse laser but with some extra nedded flags
for pump-probe simulation:
	a) Phase = X --> related to the phase of the pump (explain..)
	b) Pump = Yes  --> because this is a pump laser
	c) PumpProbeFrames = n --> number of frames during the pump dynamics
	that will be taken into account for the probes dynamics. 
	d) PumProbeRange [fs] = t_i t_f  --> these values represent the time
	window in which the probes dynamics will run. 
2. Change path to DFTB executable in `run_pumps.sh` and `run_probes.sh`
3. Change SK Files path in dftb_in.hsd_pump and dftb_in.hsd_probe
4. Run `run_pumps.sh`
5. Run `run_probes.sh`
6. Run `python genTasPhases.py`
7. Run `python plot_tas.py`
