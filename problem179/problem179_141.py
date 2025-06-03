n, m = map(int,input().split())
a = list(map(int,input().split()))

i = 0
s = 0
sum = sum(a)

for i in range(n):
    if a[i]/sum >= 1/(4*m):
        s += 1

if s >= m:
    print('Yes')

else:
    print('No')
