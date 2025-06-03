x=int(input())
cost=100
for i in range(1,10000000000):
    cost+=cost//100
    if cost>=x:
        print(i)
        break