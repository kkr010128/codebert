from sys import stdin
inp = lambda : stdin.readline().strip()

n= int(inp())
prices = [int(x) for x in inp().split()]

money= 1000
buy = -1
if prices[0] <=money: 
    buy = prices[0]
for i in range(1, len(prices)):
    if prices[i] > prices[i - 1]:
        if buy != -1:
            money = money%buy + (money//buy)*prices[i]
            buy = prices[i]
    else:
        if prices[i] < buy and prices[i] < money:
            buy = prices[i]
print(money)