n = int(input())
a = list(map(int,input().split()))
k = 1
c = 0
for i in range(n):
    if a[i] != k:
        c+=1
    elif a[i] == k:
        k += 1
if c==n:
    print(-1)
else:
    print(c)