N,K=map(int,input().split())
p=list(map(int, input().split()))
p.sort()

price=0
for idx in range(K):
    price=price+p[idx]
print(price)
