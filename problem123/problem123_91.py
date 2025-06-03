N = int(input())
a = list(map(int, input().split()))
s = 0
for i in range(N):
    s ^= a[i] 
for i in range(N):
    a[i] ^= s
for i in range(N):
    print(a[i])
