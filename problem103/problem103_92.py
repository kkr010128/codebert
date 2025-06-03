N = int(input())
A = list(map(int,input().split()))

money=1000
pos = 1
kabu = 0

for i in range(1,N):
    if A[i-1]<A[i]:
        kabu = money//A[i-1]
        money += kabu*(A[i]-A[i-1])
            
print(money)