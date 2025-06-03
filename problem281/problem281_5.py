def cmb(n, r, mod):
    if (r < 0 or r > n):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod
 
mod = 10**9+7  
nums = 10**6 # 制約に合わせよう
g1, g2, inverse = [1, 1] , [1, 1], [0, 1]
 
for num in range(2, nums + 1):
    g1.append((g1[-1] * num) % mod)
    inverse.append((-inverse[mod % num] * (mod//num)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)
    
x, y = map(int, input().split())
if (x+y)%3 or 2*x<y or 2*y<x:
    print(0)
else:
    print(cmb((x+y)//3,(2*x-y)//3, mod))