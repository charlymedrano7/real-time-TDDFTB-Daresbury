#!/usr/bin/env python3

import numpy as np
import os
from scipy import constants
import argparse
import matplotlib.pyplot as plt
hplanck = constants.physical_constants['Planck constant in eV s'][0] * 1.0E15

parser = argparse.ArgumentParser(description='Calculate pump-probe spectra from dipole trajectories')
parser.add_argument('--dir-prefix', dest='pref', help='directory where the pump folders (phase_*) are')
parser.add_argument('--pump-input', dest='pump_in', help='input file used a pump simulation (any phase)', required=True)
parser.add_argument('--probe-input', dest='probe_in', help='input file used for a probe simulation', required=True)
parser.add_argument('--nphases', type=int, dest='nphases', help='number of phases', required=True)

args = parser.parse_args()

if args.pref:
    ROOT = args.pref
else:
    ROOT = os.getcwd()

print('ROOT', ROOT)
PHASE_DIR = ROOT+'/phase_0/'

#General parameters
try:
    pumpfile = open(args.pump_in, 'r').readlines()
except FileNotFoundError:
    print('Pump file not found')
    sys.exit()

try:
    probefile = open(args.probe_in, 'r').readlines()
except FileNotFoundError:
    print('Probe file not found')
    sys.exit()

pprange_defined = False

for ll in pumpfile:
    ll_lowercase = [li.lower() for li in ll.split()]
    if "steps" in ll_lowercase:
        nsteps_pump = int(ll.split()[2])
        print ('number of steps pump = {}'.format(nsteps_pump))
    if "timestep" in ll_lowercase:
        dt = float(ll.split()[3])*0.024188 # fs
        print ('timestep = {:.4f}'.format(dt))
    if "pumpprobeframes" in ll_lowercase:
        nppframes = int(ll.split()[2])
        print ('number of pump probe frames = {}'.format(nppframes))
    if "pumpproberange" in ll_lowercase:
        probe_ini = float(ll.split()[3]) # we assume fs for the moment
        probe_fin = float(ll.split()[4]) # we assume fs for the moment
        pprange_defined = True
    
if not pprange_defined:
    probe_ini = 0
    probe_fin = nsteps_pump*dt
print ('initial time for writing pump frames = {:.1f}'.format(probe_ini))
print ('final time for writing pump frames = {:.1f}'.format(probe_fin))

for ll in probefile:
    ll_lowercase = [li.lower() for li in ll.split()]
    if "steps" in ll_lowercase:
        nsteps_spec = int(ll.split()[2])
        print ('number of steps probe = {}'.format(nsteps_spec))

damping = 7 #1/fs
cutoff_freq = 8 # eV
steps_ini = int(probe_ini/dt)
steps_fin = int(probe_fin/dt)
ndump = int((steps_fin-steps_ini)/nppframes)
nmaxspecs = nppframes

print('steps ini', steps_ini)
print('steps fin', steps_fin)
print('ndump', ndump)
def loaddata(nlines, onlyx=False):
    mux = np.loadtxt('mux.dat')
    muy = np.loadtxt('muy.dat')
    muz = np.loadtxt('muz.dat')
    return mux[:,0], mux[:,1], muy[:,2], muz[:,3]

def cutspec(freqev, spec, cutoff_freq=None):
    if cutoff_freq is None:    
        cutoff_freq = 30 #eV
    idx = np.argmin(abs(freqev-cutoff_freq))
    return freqev[:idx], spec[:idx]

def runfft(mu, time, damp, cutoff=None):
    length = time.shape[0]
    damped = np.exp(-time/damp)
    spec = np.fft.rfft(damped*mu, 10*length)
    freqev = np.fft.rfftfreq(10*length,time[1]-time[0]) * hplanck
    return cutspec(freqev, spec, cutoff)

# GS_spectrum
os.chdir(ROOT+'/gs_spectrum')
time, mux, muy, muz = loaddata(nsteps_spec)
ave = (mux-mux[0]+muy-muy[0]+muz-muz[0])/3.
freq0, fft0 = runfft(ave, time, damping, cutoff_freq)
spec0 = fft0.imag * freq0 * (-2./np.pi)
np.savetxt(ROOT+'/gs_spectrum.dat', spec0)

for phase_idx in range(args.nphases):
    PHASE_DIR = ROOT+'/phase_{}/'.format(phase_idx)
    mupump = np.genfromtxt(PHASE_DIR+'mu.dat')
    mupumpx = mupump[:, 1]
    mupumpy = mupump[:, 2]
    mupumpz = mupump[:, 3]
    time_pu = mupump[:, 0]
    dltime = np.array(time_pu[steps_ini:steps_fin:ndump])
    specs = np.zeros((nmaxspecs, fft0.size))

    for frame in range(nmaxspecs):
        print(steps_ini+frame*ndump, steps_ini+frame*ndump+nsteps_spec)
        os.chdir(PHASE_DIR+'probes/frame{}/'.format(frame))
        time, mux, muy, muz = loaddata(nsteps_spec)
        mux = mux[:-1] - mupumpx[steps_ini+frame*ndump+2: steps_ini+frame*ndump+nsteps_spec+2]
        muy = muy[:-1] - mupumpy[steps_ini+frame*ndump+2: steps_ini+frame*ndump+nsteps_spec+2]
        muz = muz[:-1] - mupumpz[steps_ini+frame*ndump+2: steps_ini+frame*ndump+nsteps_spec+2]
        ave = (mux + muy + muz)/3.
        freq, spec = runfft(ave, time[:-1], damping, cutoff_freq)
        specs[frame, :] = spec.imag * freq * (-2./np.pi)
    np.savetxt(ROOT+'/spectra_ph{}.dat'.format(phase_idx), specs)

np.savetxt(ROOT+'/delaytime.dat', dltime)
np.savetxt(ROOT+'/energy.dat', freq)
