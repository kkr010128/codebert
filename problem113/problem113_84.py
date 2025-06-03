from random import randint
D = int(input())
C = [int(T) for T in input().split()]
S = [[] for TD in range(0,D)]
for TD in range(0,D):
    S[TD] = [int(T) for T in input().split()]
SatM = 0
TesM = [1]*D
for TV in range(0,1000):
    Type = 26
    Last = [0]*Type
    SatS = 0
    Test = [randint(1,26) for TD in range(0,D)]
    for TD in range(0,D):
        Last[Test[TD]-1] = TD+1
        SatS += S[TD][Test[TD]-1]
        for TC in range(0,Type):
            SatS -= C[TC]*(TD+1-Last[TC])
    if SatS>SatM:
        SatM = SatS
        TesM = Test
print('\n'.join(str(TD) for TD in TesM))