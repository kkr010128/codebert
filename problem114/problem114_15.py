D = int(input())
C = [int(T) for T in input().split()]
S = [[] for TD in range(0,D)]
for TD in range(0,D):
    S[TD] = [int(T) for T in input().split()]
Type = 26
Last = [0]*Type
SatD = [0]*D
SatA = [0]*(D+1)
for TD in range(0,D):
    Test = int(input())-1
    Last[Test] = TD+1
    SatD[TD] = S[TD][Test]
    for TC in range(0,Type):
        SatD[TD] -= C[TC]*(TD+1-Last[TC])
    SatA[TD+1] = SatA[TD]+SatD[TD]
print('\n'.join(str(T) for T in SatA[1:]))