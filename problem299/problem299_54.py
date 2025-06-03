n = int(input())

a = [int(e) for e in input().split()]

ans = [0] * n   
 
for i in range(n):
    s = a[i]   
    ans[s-1] = i+1    
 
print(*ans)