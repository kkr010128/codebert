import itertools
N, M = map(int, input().split())
print( len([i for i in list(itertools.combinations(([2]*N)+([3]*M), 2)) if sum(i) % 2 == 0]) )
