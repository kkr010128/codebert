from itertools import combinations_with_replacement as R

N,M,Q = map(int, input().split())
L = [tuple(map(int, input().split())) for _ in range(Q)]

print(max([sum((d if S[b-1] - S[a-1] == c else 0) for a,b,c,d in L) for S in R(range(1, M+1), N)]))