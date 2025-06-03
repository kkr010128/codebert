n = int(input())
a = list(map(int,input().split()))
s = 1
p = 0

for i in range(n):
    if a[i] == s:
        s += 1
    else:
        p += 1

if p == n:
    print(-1)
else:
    print(p)