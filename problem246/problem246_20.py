import itertools

N=int(input())
P=tuple(map(int,input().split()))
Q=tuple(map(int,input().split()))


prm = list(itertools.permutations(range(1,N+1)))

i = 0
for t in prm:
    i += 1
    if t == P:
        a = i
    if t == Q:
        b = i
print(abs(a-b))
