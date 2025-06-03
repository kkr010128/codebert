K = int(input())
N = 10**6
a = [0] * N

a[0] = 7
for i in range(1, N):
    a[i] = (a[i-1] * 10 + 7) % K
a[0] %= K
for i in range(N):
    if a[i] == 0:
        print(i+1)
        break
else:
    print(-1)