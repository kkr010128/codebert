import itertools

N = int(input())

P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

cntP = 0
cntQ = 0

for i in itertools.permutations(range(1,N+1)):
    if i == P:
        break
    cntP += 1

for i in itertools.permutations(range(1,N+1)):
    if i == Q:
        break
    cntQ += 1

print(abs(cntP - cntQ))