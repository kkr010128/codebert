n,k=list(map(int,input().split()))
prices=list(map(int , input().split()))
prices.sort()
amount=0
for i in range(0,k):
    amount+=prices[i]
    
    
print(amount)