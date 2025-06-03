n = int(input())
A = list(map(int, input().split()))

cnt = 0
money = 1000
b = 0
for i in range(n-1):
    if cnt == 0 and A[i] < A[i+1]:
        cnt += money//A[i]
        money %= A[i]
        b = A[i]
    else:
        money += cnt * A[i]
        cnt = 0
        if A[i] < A[i+1]:
            cnt += money//A[i]
            money %= A[i]
            b = A[i]
if cnt > 0:
    money += cnt * max(b, A[-1])
print(money)