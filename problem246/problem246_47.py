import itertools 
N = int(input())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))
w = 0
x = 0
S = []
T = []
for i in range(N):
    S.append(i+1)
for j in itertools.permutations(S):
    T.append(list(j))
a = T.index(P)
b = T.index(Q)
print(abs(a-b))
