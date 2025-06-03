from itertools import permutations

N = int(input())
P = tuple([int(s) for s in input().split()])
Q = tuple((int(s) for s in input().split()))

seqs = []
for i, x in enumerate(permutations(range(1, N + 1), N)):
    if x == P:
        p = i + 1
    
    if x == Q:
        q = i + 1
print(abs(p-q))