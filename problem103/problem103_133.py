N=int(input())
A = list(map(int, input().split()))
money=1000
stock=0
if A[0]<A[1]:
    stock=int(money/A[0])
    money=money-A[0]*stock
for i in range(1,N-1):
    if A[i-1]<A[i]:
        money=money+A[i]*stock
        stock=0
    if A[i]<A[i+1]:
        stock=int(money/A[i])
        money=money-A[i]*stock
money=money+A[N-1]*stock        
print(money)