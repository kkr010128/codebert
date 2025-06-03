N = int(input())
A = list(map(int,input().split()))

money=1000
best = money
pos = 1
kabu = 0

#初動 買うか買わないか
if A[0]<=A[1]:
    kabu = money//A[0]
    money -= kabu*A[0]
    pos=0
else:
    pos=1

#二回目以降　買うか売るか保留か
for i in range(1,N):
    if pos==0:#売り
        if A[i-1]>=A[i]:
            money+=kabu*A[i-1]
            kabu=0
            pos=1
    elif pos==1:#買い
        if A[i-1]<A[i]:
            kabu = money//A[i-1]
            money -= kabu*A[i-1]
            pos=0
            
    best = max(best,money+kabu*A[i])
            
print(best)