n, m = map(int,input().split())
A = list(map(int,input().split()))
sum = 0
count = 0
for a in A:
    sum += a
for a in A:
    if a >= sum/(4*m):
        count += 1
if count >= m:
    print('Yes')
else:
    print('No')