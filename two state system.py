from pylab import *
import math
import scipy

# Vector of beta values.
B = 1/linspace(0,3,1000)

# Partition function (non interacting and identical particles).
Z = math.exp(-B)/(1 + math.exp(-B))


