from sys import stdin
from math import ceil, floor
n = stdin.readline().rstrip()
data = [int(x) for x in stdin.readline().rstrip().split()]
m = sum(data) / len(data)
cm = ceil(m)
fm = floor(m)
ceil_m = floor_m = 0
for i in data:
    ceil_m += (i-cm)**2
    floor_m += (i-fm)**2
print(min(ceil_m, floor_m))