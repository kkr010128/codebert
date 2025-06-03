D = int(input())
C = [int(T) for T in input().split()]
S = [[] for TD in range(0,D)]
for TD in range(0,D):
    S[TD] = [int(T) for T in input().split()]
for TD in range(0,D):
    print(S[TD].index(max(S[TD]))+1)