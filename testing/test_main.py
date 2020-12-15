import unittest
import numpy as np
from main import *

class UnitTests(unittest.TestCase) :
    def test_eng(self) :
        for i in range(2**5) :
            num, spins = i, 5*[0]
            for j in range(5) :
                spins[j] = np.floor( num / 2**(4-j) )
                num = num - spins[j]*2**(4-j)
                if spins[j]==0 : spins[j] = -1
            energy = -spins[0]*spins[len(spins) - 1 ]
            for i in range(0,len(spins)-1) : energy = energy - spins[i]*spins[i+1]
            self.assertTrue( hamiltonian( spins )==energy, "Hamiltonian gives the wrong value for the energy" )
