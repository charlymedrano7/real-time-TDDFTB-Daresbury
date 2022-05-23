#!/usr/bin/env python3

'''
Charge per fragment of DFTB+ TD data
'''

import sys
import optparse
import numpy as np

USAGE = """usage: %prog -d xx

Reads output from TD calculation (after laser) and produces charge per fragment requested.

Needs qsvst.dat file in working directory."""

def main():
    parser = optparse.OptionParser(usage=USAGE)
    parser.add_option("-n", "--natoms", action="store", dest="natoms",
            help="number of atomsi in the system")
    parser.add_option("-l", "--list", action="store", dest="list",
            help="list of atom indexes defining the fragments.") 

    (options, args) = parser.parse_args()

    print(options.list)
    list_index = options.list.split()

    nfrag = int(len(list_index)-1)          #number of fragments   
    qsdata = np.genfromtxt('qsvst.dat')
    time = qsdata[:,0]
    q_fragments = [0]*nfrag
    
    for i in range(nfrag):       #sum of the atomic charges inside each fragment
        print(i)
        q_fragments[i] = qsdata[:,2+int(list_index[i:i+2][0]):2+int(list_index[i:i+2][1])].sum(axis=1) 
        np.savetxt("charge_frag%s.dat"%(i+1), np.column_stack((time, q_fragments[i]-q_fragments[i][0])))

if __name__ == "__main__":
    main()

