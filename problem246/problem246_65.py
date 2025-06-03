import itertools

N = int(input())

l = []

for i in itertools.permutations(list(range(1,N+1))):
    l.append(i)

P = tuple(map(int,input().split()))
Q = tuple(map(int,input().split()))

a = 1
b = 1

for i in l:
    if i < P:
        a += 1

for i in l:
    if i < Q:
        b += 1

print(abs(a-b))