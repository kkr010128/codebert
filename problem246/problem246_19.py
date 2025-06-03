import itertools
n=int(input())
a=[]
for i in range(n):
    a.append(i+1)
b=[]
for per in itertools.permutations(a):
    b.append(list(per))
c=b.index(list(map(int,input().split())))
d=b.index(list(map(int,input().split())))
print(abs(c-d))