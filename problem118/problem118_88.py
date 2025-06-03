N=int(input())
ans = 0
for k in range(1,N+1):
    n_ = N // k
    ans_ = k*n_*(n_+1)//2
    ans+= ans_
print(ans)