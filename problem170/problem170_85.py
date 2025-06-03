n,k = map(int,input().split())
mod = 10**9+7
from itertools import accumulate
N = list(range(n+1))
N_acc = [0]+list(accumulate(N))
ans = 0
for i in range(k,n+2):
    ans += ((N_acc[-1]-N_acc[-i-1])-N_acc[i]+1)%mod
print(ans%mod)