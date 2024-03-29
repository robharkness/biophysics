import numpy as np

# P + L <-> PL
def twostatebinding(C, constants):

    k1, km1 = constants
    R = []
    R.append([-k1*C[1], 0, km1]) # P
    R.append([-k1*C[1], 0, km1]) # L
    R.append([k1*C[1], 0, -km1]) # PL

    return R

# Enzyme catalyzing a substrate, E + S <-> ES -> E + P
def michaelismenten(C, constants):

    k1,km1,kcat = constants
    R = []
    R.append([-k1*C[1], 0, 0, (km1+kcat)]) # E
    R.append([-k1*C[1], 0, 0, km1]) # S
    R.append([0, 0, 0, kcat]) # P
    R.append([k1*C[1], 0, 0, (-km1-kcat)]) # ES

    return R

# All forms of bound trimer can catalyze
def equilibrium_trimer(C, constants):

    kcat = constants
    R = []
    R.append([-kcat, -2*kcat, -3*kcat])
    R.append([kcat, 2*kcat, 3*kcat])

    return R
    

