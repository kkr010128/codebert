from itertools import permutations
n=int(input())
p=list(map(int,input().split()))
q=list(map(int,input().split()))
c=sorted(list(permutations(range(1,n+1))))
a,b,=0,0
for i,c in enumerate(c):
    if p==list(c):
        a=i
    if q==list(c):
        b=i
print(abs(a-b))