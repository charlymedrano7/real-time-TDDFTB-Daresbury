import numpy as np
import matplotlib.pyplot as plt
from scipy import constants
import os

def loadSpecs(ROOT, nphases):
    delay_time = np.genfromtxt(ROOT+'delaytime.dat')
    freq = np.genfromtxt(ROOT+'energy.dat')
    spec0 = np.genfromtxt(ROOT+'gs_spectrum.dat')
    specs = []
    for ph in range(nphases):
        specs.append(np.genfromtxt(ROOT+'spectra_ph{}.dat'.format(ph)))
    return freq, delay_time, specs, spec0

class specData():
    def __init__(self, ROOT, nphases):
        en, dlt, spec, spec0 = loadSpecs(ROOT, nphases)
        self.energies = en
        self.delaytime = dlt
        self.spec = spec
        self.spec0 = spec0
        self.nphases = nphases
        self.avespec = sum(self.spec[:])/self.nphases
        self.tas = self.avespec - self.spec0
        
def plotTasAxis(axx, specs, freq, delaytime, vmax=None):
    im = axx.imshow(specs, aspect='auto', interpolation='hanning',
              cmap=plt.get_cmap('jet'), extent=[freq.min(), freq.max(), delaytime.max(), delaytime.min()])
    axx.set_xlabel('energy / eV')
    axx.set_ylabel('delay time / fs')
    return im 

tas_data = specData('./', 4)
plt.figure()
plt.plot(tas_data.energies, tas_data.spec0)
plt.title('Ground state spectrum')
plt.savefig('gs_spectrum.png' , dpi=200)
plt.show()

fig, ax = plt.subplots(figsize=(9, 8))
im = plotTasAxis(ax, tas_data.tas, tas_data.energies, tas_data.delaytime)
fig.colorbar(im, ax=ax)
ax.axvline(3.80, c='w', lw=3)
ax.set_xlim(1.0, 8.0)
plt.savefig('tas.png' , dpi=200)
plt.show()

