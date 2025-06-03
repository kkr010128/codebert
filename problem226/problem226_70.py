#153_B
h, n = map(int, input().split())
a = list(map(int, input().split()))

sum = 0
for i in range(n):
    sum += a[i]
    
if sum >= h:
    print('Yes')
else:
    print('No')