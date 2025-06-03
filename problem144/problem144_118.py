import numpy as np

raw = input()
rawl = raw.split()
A = int(rawl[0])
B = int(rawl[1])
H = int(rawl[2])
M = int(rawl[3])
theta = 2*np.pi*(H/12+M/720-M/60)
print((A*A+B*B-2*A*B*np.cos(theta))**(0.5))
