#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

# pi_hex.txt  = 1e6 digits in binary

# Load hex digits from file
f = open('pi_hex.txt', 'r')
chars = f.read()[2:] # Skip 3.

# Number of binary digits
N = len(chars) * 4

# Set aside some memory
S = 1 # Step size
R = np.arange(1, N+1, S)
X = np.ndarray(shape=( int(N/S) ), dtype=float)

# Iterated logarithm test
itlog = np.sqrt(2 * np.log( np.log( R ) ) / R)

print(itlog)

Xprev = 0
k = 0
n = 1
for hex_char in chars:
    as_bin = (bin(int(hex_char, 16))[2:]).zfill(4)
    for b in as_bin:
        Xprev = ( Xprev*(n-1) + 2*int(b)-1 ) / n
        if (n - 1) % S == 0:
            # Store this entry
            X[k] = Xprev
            k = k + 1
        n = n + 1

plt.gca().set_xscale('log')
plt.plot(R, X, '-k', R, itlog, '--k', R, -itlog, '--k')

plt.show()
