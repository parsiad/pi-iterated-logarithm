#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import getopt, sys

def usage():
    print(sys.argv[0] + """ [-f FILE] [-s STEP]

-f FILE | --file FILE
        Uses the file located at path FILE for the digits of Pi. Default is
        pi_hex_250000.txt, which gives the first million binary digits of Pi
        stored in hexadecimal.

        Note, file must be stored in hexadecimal. See pi_hex_250000.txt for an
        example.

-s STEP | --step-size STEP
        Only stores N/STEP elements in memory to produce plots. Useful if the
        number of digits is large.
""")

def main():

    ############################################################################

    # Default options
    S = 1
    file = 'pi_hex_250000.txt'

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hs:f:", ["help", "step-size=",
                "file="])
    except getopt.GetoptError as err:
        # Print help and exit
        print(str(err))
        usage()
        sys.exit(2)
    for o, a in opts:
        if o in ("-f", "file="):
            file = a
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-o", "--step-size"):
            S = a
        else:
            assert False, "unhandled option"

    ############################################################################

    # Load hex digits from file
    f = open(file, 'r')
    chars = f.read()[2:] # Skip 3.

    # Number of binary digits
    N = len(chars) * 4

    # Set aside some memory
    R = np.arange(1, N+1, S)
    X = np.ndarray(shape=( int(N/S) ), dtype=float)

    # Iterated logarithm test
    with np.errstate(divide='ignore'):
        with np.errstate(invalid='ignore'):
            itlog = np.sqrt(2 * np.log( np.log( R ) ) / R)

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

if __name__ == "__main__":
    main()
