from itertools import permutations
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

l=[i+1 for i in range(n)]
perm = permutations(l)
perm=list(perm)
p=[]
for i in perm:
    k=(''.join(map(str,i)))
    p.append(int(k))
a=''.join(map(str,a))
b=''.join(map(str,b))
idx1=p.index(int(a))
idx2=p.index(int(b))
print(abs(idx1-idx2))