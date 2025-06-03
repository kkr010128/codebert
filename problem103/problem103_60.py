N = int(input())
A = [int(x) for x in input().split()]

money = 1000
s = 0
for i in range(N - 1):
    # begginig of i-th day
    # sell all of stocks
    money += s * A[i]
    s = 0

    if A[i] < A[i + 1]:
        s = money // A[i]
        money %= A[i]

    # print('end of {0}-th day, money: {1}, stock: {2}'.format(i, money, s))

money += s * A[-1]
print(money)