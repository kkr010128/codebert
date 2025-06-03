import sys

input = sys.stdin.buffer.readline

n = int(input())
# n+1個
A = list(map(int, input().split()))

if n == 0:
    if A[0] == 1:
        print(1)
    else:
        print(-1)
    exit()
if A[0] > 0:
    print(-1)
    exit()

ans = 0
max2 = 0
kouho = [0] * (n + 1)
for i in range(n, 0, -1):
    max1 = pow(2, i)
    max2 += A[i]
    max2 = min(max1, max2)
    kouho[i] = max2
kouho[0] = 1
not_leave = 1
for i in range(1, n + 1):
    cnt = 0
    not_leave *= 2
    temp = min(kouho[i], not_leave)
    ans += temp
    not_leave -= A[i]
    if not_leave <= 0 and i != n:
        print(-1)
        exit()
    if i == n:
        if not_leave == 0:
            continue
        elif not_leave < 0:
            print(-1)
            exit()
ans += 1
print(ans)
