n = int(input())
p = tuple(map(int,input().split()))
q = tuple(map(int,input().split()))

import itertools

li = [i for i in range(1,n+1)]
li2 = list(itertools.permutations(li))

cnt = 0
for i in li2:
    cnt +=1
    if i == p:
        a = cnt
    if i == q:
        b = cnt

print(abs(a-b))