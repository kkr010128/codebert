D = int(input())
C = [int(T) for T in input().split()]
S = [[] for TD in range(0,D)]
for TD in range(0,D):
    S[TD] = [int(T) for T in input().split()]
Type = 26
Last = [0]*Type
Sats = 0
for TD in range(0,D):
    Test = int(input())-1
    Last[Test] = TD+1
    Sats += S[TD][Test]
    for TC in range(0,Type):
        Sats -= C[TC]*(TD+1-Last[TC])
    print(Sats)