import time
start = time.time()
n = int(input())
a = list(map(int,input().split()))
b = []
m = 0
for i in range(1,n):
    m = m ^ a[i]
b.append(m)
for j in range(1,n):
    m = m ^ a[j-1]
    m = m ^ a[j]
    b.append(m)
b = map(str,b)
print(' '.join(b))