from itertools import permutations

input()
P = int(''.join(input().split()))
Q = int(''.join(input().split()))

s = sorted(permutations(str(P)))
pi = s.index(tuple(str(P)))
qi = s.index(tuple(str(Q)))

print(abs(pi - qi))