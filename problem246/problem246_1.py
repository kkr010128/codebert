import itertools
a=int(input())
b=list(map(int,input().split()))
c=list(map(int,input().split()))

n=sorted(b)
m=list(itertools.permutations(n))
m=[list(i) for i in m]
print(abs(m.index(b)-m.index(c)))