n = int(input())

A = list(map(int,input().split()))

ans = 0
for i,a in enumerate(A):
    if (i+1)%2 != 0 and a%2 != 0:
        ans +=1
        
print(ans)