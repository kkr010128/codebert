import math
n,D = map(int,input().split())
cnt = 0
for i in range(n):
    p,q = map(int,input().split())
    d = math.sqrt(p**2 + q ** 2)
    if D >= d:
        cnt += 1
print(cnt)