N = int(input())
An = list(map(int, input().split()))
money = 1000
stock = 0
for i in range(N-1):
    if An[i+1] > An[i]:
        stock = money // An[i]
        money += (An[i+1] - An[i]) * stock
print(money)
