n = int(input())
oi = list(map(int,input().split()))

total = 0
for i in range(n-1):
    for j in range(i+1,n):
        total += oi[i]*oi[j]
        
print(total)