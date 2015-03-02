pi-iterated-logarithm
=====================
A numerical test to see if the digits of Pi satisfy the iterated logarithm.

Example output
--------------

![Alt text](https://raw.githubusercontent.com/parsiad/pi-iterated-logarithm/master/figure_1.png)

Requirements
------------

- matplotlib
- numpy

Usage
-----

```
./pi_iterated_logarithm.py [-f FILE] [-s STEP]

-f FILE | --file FILE
        Uses the file located at path FILE for the digits of Pi. Default is
        pi_hex_250000.txt, which gives the first million binary digits of Pi
        stored in hexadecimal.

        Note, file must be stored in hexadecimal. See pi_hex_250000.txt for an
        example.

-s STEP | --step-size STEP
        Only stores N/STEP elements in memory to produce plots. Useful if the
        number of digits is large
```