n = int(input())
A = list(map(int,input().split()))

groups = []
prev = A[0]
for i in range(1,n):
    if A[i] != prev:
        groups.append(prev)
        prev = A[i]
groups.append(prev)

if len(groups) == 1:
    print(1000)
    exit()

money = 1000
stock = 0
if groups[0] < groups[1]:
    buy = money//groups[0]
    stock += buy
    money -= groups[0]*buy
    
for i in range(1,len(groups)-1):
    if groups[i-1] < groups[i] and groups[i] > groups[i+1]:# 周辺の最高値
        money += stock*groups[i]
        stock = 0
    elif groups[i-1] > groups[i] and groups[i] < groups[i+1]:# 周辺の最安値
        buy = money//groups[i]
        stock += buy
        money -= groups[i]*buy

money += stock*groups[-1]

print(money)