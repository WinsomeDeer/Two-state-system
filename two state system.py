from pylab import *
import math
import scipy

# Vector of beta values.
B = linspace(0,3,1000)

# Average energy function (non interacting and identical particles).
E = exp(-1/B)/(1 + exp(-1/B))
CV = diff(E)/diff(B)

# Create subplots.
subplot(2,1,1)
plot(B,E)
xlabel('kT'), ylabel('E')
xmid = 0.5*((B[1:])+B[0:-1])
subplot(2,1,2)
plot(xmid, CV)
xlabel('kT'), ylabel('CV')
show()
