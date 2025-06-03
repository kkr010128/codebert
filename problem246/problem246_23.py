from itertools import permutations
n=int(input())
p=tuple(int(i)for i in input().split())
q=tuple(int(i)for i in input().split())
permutation_n=list(permutations(range(1,n+1)))
a=b=0
for i in permutation_n:
    if i<p:a+=1
    if i<q:b+=1
print(abs(a-b))