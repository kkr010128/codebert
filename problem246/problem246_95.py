import itertools

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
per = list(itertools.permutations(sorted(P)))

print(abs(per.index(tuple(P)) - per.index(tuple(Q))))