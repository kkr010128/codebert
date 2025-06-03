import itertools

n,k=map(int,input().split())
d=[]
a=[]
for i in range(k):
    d.append(int(input()))
    a.append(list(map(int,input().split())))
a_1=itertools.chain.from_iterable(a)
print(n-len(list(set(a_1))))