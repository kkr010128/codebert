N = int(input())
ans = 10**100

for i in range(1,int(N**(0.5))+1):
    if N % i == 0:
        tmp = (i-1) + (N//i -1)
    
    ans = min(ans,tmp)

print(ans)
