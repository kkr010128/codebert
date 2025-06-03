N = int(input())
A = list(map(int,input().split()))

ans =1
mod = 10**9+7
row = [0] *3
for i in range(N):
    
    ans *=row.count(A[i])
    ans %=mod
    for j in range(3):
        if row[j]==A[i]:
            row[j]+=1
            break
    

        
print(ans%mod)