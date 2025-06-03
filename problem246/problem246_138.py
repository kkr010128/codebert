import itertools
n=int(input())
p=tuple(map(int, input().split()))
q=tuple(map(int, input().split()))

per=itertools.permutations(range(1, n+1), n)
for i, v in enumerate(per):
    if(p==v): pi=i
    if(q==v): qi=i

print(abs(pi-qi))
