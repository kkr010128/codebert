import itertools
a=int(input())
b=tuple(map(int,input().split()))
c=tuple(map(int,input().split()))
d=list(itertools.permutations(range(1,a+1)))
print(abs(d.index(b)-d.index(c)))