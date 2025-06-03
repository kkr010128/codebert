n = int(input())
a = list(map(int,input().split()))
q = int(input())
m = list(map(int,input().split()))

s = [list(map(int,bin(x)[2:].zfill(n))) for x in range(2**n)]

anset=set()
for j in s:
    ans=0
    for k in range(n):
        ans+=a[k]*j[k]
    anset.add(ans)

for i in range(q):
    if m[i] in anset:
        print('yes')
    else:
        print('no')

