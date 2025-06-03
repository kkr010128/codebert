N = int(input())
a = list(map(int,input().split()))
b = N
num = 1
for i in range(N):
    if a[i] == num:
        num += 1
        b -= 1
if b == N:
    print(-1)
else:
    print(b)