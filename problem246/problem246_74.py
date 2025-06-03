from itertools import permutations

n = int(input())
l = [tuple(map(int,input().split())) for _ in range(2)]
a = list(permutations(range(1,n+1)))
print(abs(a.index(l[0]) - a.index(l[1])))