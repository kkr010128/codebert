N,K = map(int,input().split())
p = list(map(int,input().split()))
math = [0]*N
ans = 0
check = 0
for i,j in enumerate(p):
    math[i] += (j*(j+1)/2)/j
    if(i+1<=K):
        check += math[i]
    else:
        check += math[i]
        check -= math[i-K]
    ans = max(ans,check)
print(ans)