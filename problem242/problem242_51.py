import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N,K = MI()
A = [-10**10] + LI()
A.sort()

mod = 10**9+7

B = [0]*(K-1) + [1]  # B[i] = i_C_(K-1)
for i in range(K,N):
    B.append((B[-1]*i*pow(i-(K-1),mod-2,mod)) % mod)

ans = 0
for i in range(1,N+1):
    ans += (B[i-1]-B[N-i])*A[i]
    ans %= mod
print(ans)
