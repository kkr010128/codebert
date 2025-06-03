n,k=map(int,input().split())
price=list(map(int,input().split()))

s_price=sorted(price)

mysum=0

for i in range(k):
  mysum+=s_price[i]
  
print(mysum)