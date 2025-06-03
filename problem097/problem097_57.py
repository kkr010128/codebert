import sys

K = int(input())
a = []
i = 1

a.append(7 % K)
while i < K:
    a.append((a[i-1]*10+7) % K)
    i += 1

i = 0
while i < K:
    if(a[i]==0):
        print(i+1)
        exit(0)
    i += 1

print(-1)