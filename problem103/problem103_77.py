N = int(input())
A = list(map(int, input().split()))

iStock = 0
iMoney = 1000

for i in range(N-1):
    if A[i] < A[i + 1]:
        # A[i]Day 株購入 & A[i+1]Day 株売却
        iStock = iMoney // A[i]
        iMoney %= A[i]
        iMoney += iStock * A[i+1]
print(iMoney)