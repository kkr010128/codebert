import math

A, B, H, M = map(int, input().split())
minutes = H*60 + M
shortArg = 0.5 * minutes
#print(shortArg)
longArg = 6 * M
#print(longArg)

arg = abs(shortArg - longArg)
C2 = A**2 + B**2 - 2 * A * B * math.cos(math.radians(arg))

#print(math.cos(math.radians(arg)))

print(C2**(1/2))