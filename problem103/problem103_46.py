n = int(input())
A = list(map(int, input().split()))

money = 1000
kabu = 0
memo = []

buy = True

for i in range(n-1):
    if buy:
        if A[i] < A[i+1]:
            kabu = money //A[i]
            money %= A[i]
            buy = False
    else:
        if A[i] > A[i+1]:
            money += kabu * A[i]
            kabu = 0
            buy = True

if kabu:
    money += kabu * A[n-1]

print(money)