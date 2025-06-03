import itertools
n =int(input())
p =tuple(map(int,input().split()))
q =tuple(map(int,input().split()))

l = list(range(1,n+1))
r = list(itertools.permutations(l, n))

print(abs(r.index(p)-r.index(q)))