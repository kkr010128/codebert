import itertools

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

tmp = [n+1 for n in range(N)]

parms = list(itertools.permutations(tmp, N))

for i in range(len(parms)):
    if parms[i] == P:
        a = i
    if parms[i] == Q:
        b = i
        
print(abs(a-b))