N = int(input())
a = list(map(int, input().split()))
num0 = 0
num1 = sum(a)

ans = 10**10
for i in range(0, N):
    num0 += a[i]
    num1 -= a[i]
    if ans > abs(num1-num0):
        ans = abs(num1-num0)
print(ans)
