# Introducing interacting spins

In the previous exercise you wrote a program to calculate the Hamiltonian for a system of non-interacting spins interacting with an external magnetic field.  In this exercise we are now going to write a Hamiltonian for a system of interacting spins.  These spins are going to be arranged on a ring and each spin will interact with its two nearest neighbours.  The Hamiltonian is thus:

![](https://render.githubusercontent.com/render/math?math=E=-\sum_{i=1}^Ns_is_{i%2B1})

and notice that ![](https://render.githubusercontent.com/render/math?math=s_{N%2B1}=s_1) because, as detailed earlier, the spins are arranged on a ring.

Modify the code in `main.py` so that the function called `hamiltonian` calculates the the quantity defined by the formula above.  Notice that this function takes a list called `spins`, which contains all the spin coordinates.
