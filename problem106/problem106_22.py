import math

N = int(input())

#f(n) を以下の 2 つの条件の両方を満たすような 3 つの整数の組 (x,y,z)の個数とします。
# 1≤x,y,z
# x**2 + y**2 + z**2 + xy + yz + zx = n

# x,y,zの最大値を考える。
# x**2 + 1**2 + 1**2 + x + 1 + x = n
# x**2 + 2x = n - 3
# x**2 + 2x -n + 3 = 0
# x = {-2 ± sqrt(2**2 - 4*1*(-n+3))}/2*1
# x = {-2 ± sqrt(4 + 4n -12)}/2
# 1 ≤ xより
# x = {-2 + sqrt(4n - 8)}/2 = {-2 + 2 * sqrt(n - 2)}/2 = -1 + sqrt(n - 2)
# ∴ 1 ≤ x ≤ math.floor(-1 + sqrt(n - 2))
# y,zも同様。
# N <= 10**4 より、x,y,xで全探索しても(10**2)**3 = 10**6 で間に合う

ans_dict = {i:set() for i in range(1,N+1)}

if N != 1:
    for i in range(1,1 + math.floor(-1 + math.sqrt(N - 2))):
        for j in range(1,1 + math.floor(-1 + math.sqrt(N - 2))):
            for k in range(1,1 + math.floor(-1 + math.sqrt(N - 2))):
                n = i**2 + j**2 + k**2 + i*j + j*k + k*i
                if 1 <= n <= N:
                    ans_dict[n].add((i,j,k))
                
    for i in range(1,N+1):
        print(len(ans_dict[i]))
else:
    print(0)