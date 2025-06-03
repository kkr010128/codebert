from itertools import permutations

n = int( input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

a = [i for i in range(1,n+1)]



x = list(permutations(a,n))

y = x.index(p)
z = x.index(q)

print(abs(y-z))


