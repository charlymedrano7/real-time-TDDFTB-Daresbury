#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(description='Plot transient absorption spectra')
parser.add_argument('--ref-time', type=float, dest='ref_time', help='Time of the reference spectrum', default=0.0)
parser.add_argument('--pump-energy', type=float, dest='pump_energy', help='Laser energy of the pump', required=True)
parser.add_argument('--time-range', type=float, nargs='+',dest='dltime_range', help='Range of delay times in fs', required=True)
parser.add_argument('--energy-range', type=float, nargs='+',dest='en_range', help='Range of energies in eV', required=True)

args = parser.parse_args()

def loadSpecs(ROOT, nphases):
    delay_time = np.genfromtxt(ROOT+'delaytime.dat')
    freq = np.genfromtxt(ROOT+'energy.dat')
    spec0 = np.genfromtxt(ROOT+'gs_spectrum.dat')
    avespec = np.genfromtxt(ROOT+'average_spec.dat')
    return freq, delay_time, avespec, spec0

class specData():
    def __init__(self, ROOT, nphases):
        en, dlt, avespec, spec0 = loadSpecs(ROOT, nphases)
        self.energies = en
        self.delaytime = dlt
        self.spec0 = spec0
        self.avespec = avespec
        self.tas = self.avespec - self.spec0
        laser_data = np.genfromtxt(ROOT+'phase_0/laser.dat')
        self.l_time = laser_data[:,0]
        self.laser = laser_data[:,1:]
        
def plotTasAxis(axx, specs, freq, delaytime, vmax=None):
    im = axx.imshow(specs, aspect='auto', interpolation='hanning', vmax=vmax, vmin=-vmax,
              cmap=plt.get_cmap('jet'), extent=[freq.min(), freq.max(), delaytime.max(), delaytime.min()])
    axx.set_xlabel('energy / eV')
    axx.set_ylabel('delay time / fs')
    return im 

tas_data = specData('./', 4)
ref_time_idx = np.argmin(abs(tas_data.delaytime - args.ref_time))

fig, ax = plt.subplots(figsize=(9, 8))
vmax = (tas_data.avespec[-1] - tas_data.avespec[ref_time_idx]).max()
im = plotTasAxis(ax, tas_data.avespec-tas_data.avespec[ref_time_idx], tas_data.energies, tas_data.delaytime, vmax=vmax)
fig.colorbar(im, ax=ax)

ax2 = fig.add_axes([0.12, 0.95, 0.63, 0.2])
ax2.plot(tas_data.energies, tas_data.spec0, label='GS')
ax2.plot(tas_data.energies, tas_data.avespec[-1], label='last recorded')
ax.set_xlim(args.en_range[0],args.en_range[1])
ax2.set_xlim(args.en_range[0],args.en_range[1])
ax.axvline(2.3, c='k', linestyle='--')
ax2.axvline(2.3, c='k', linestyle='--')

ax3 = fig.add_axes([-0.15, 0.12, 0.2, 0.76])
ax3.plot(tas_data.laser[:,0], tas_data.l_time)
ax.set_ylim(args.dltime_range[1], args.dltime_range[0])
ax3.set_ylim(args.dltime_range[1], args.dltime_range[0])
plt.savefig('tas.png' , dpi=200, bbox_inches='tight')
plt.show()

