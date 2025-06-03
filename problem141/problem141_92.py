from itertools import accumulate

n = int(input())
a = list(map(int, input().split()))

if n == 0:
    print(1 if a[0] == 1 else - 1)
    exit()

if a[0] != 0:
    print(-1)
    exit()

b = list(accumulate(a))
v = 1
cnt = 1
for i in range(n):
    if (v - a[i]) * 2 - a[i + 1] < 0:
        print(-1)
        exit()
    v = min((v - a[i]) * 2, b[-1] - b[i])
    cnt += v
print(cnt)