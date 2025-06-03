import math
def S(i):
    return ((i * (i+1)) // 2)

N = int(input())
ans = 0
sqrt_N = math.floor(math.sqrt(N))

for K in range(1, N+1, 1):
    if((N // K) < sqrt_N):
        break
    # 個別に足す
    ans += S(N // K) * K

for NdivK in range(1, sqrt_N, 1):
    # [N // K]が等しいKの区間を求める
    Kbegin = N // (NdivK + 1)
    Kend = N // NdivK
    ans += (S(NdivK) * (S(Kend) - S(Kbegin)))

print(ans)