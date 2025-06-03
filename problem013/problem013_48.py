import math
A = []
N = int(input())
maxdiff = 0
for n in range(N):
    A.append(int(input()))
R = tuple(A)

Dmax = R[1] -R[0]
Rmin = R[0]

for i in range(1, N):
    if R[i] >= R[i-1]:
        if R[i] - Rmin > Dmax:
            Dmax = R[i] -Rmin
    if R[i] < Rmin:
        Rmin = R[i]
#    print(R[i], Dmax, Rmin)

print(Dmax)