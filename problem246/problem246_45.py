import itertools
N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))
R = [i+1 for i in range(N)]
RPS = sorted(list(itertools.permutations(R)))
print(abs(RPS.index(P)-RPS.index(Q)))