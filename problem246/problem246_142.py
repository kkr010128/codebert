from itertools import permutations
N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

p = sorted(list(permutations(P)))
q = sorted(list(permutations(Q)))

print(abs(p.index(P) -  q.index(Q)))




