a,b = [int(i) for i in input().split()]
l =  [int(i) for i in input().split()]
ans = [10**9 for _ in range(a+1)]       
ans[0] = 0          

for i in range(a+1):
    for j in l:
        if i + j < a+1:
            ans[i+j] = min(ans[i] + 1,ans[i+j])
            
print(ans[-1])
