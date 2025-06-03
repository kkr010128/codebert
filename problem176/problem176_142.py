n, k = map(int, input().split())
mod = 10**9 + 7
s = [0 for i in range(k+1)]
ret = 0

for i in range(k, 0, -1):
    p = int(k/i)
    c = pow(p, n, mod)
    for j in range(2, k+1):
        if i*j <= k:
            c -= s[i*j]
        else:
            break
    
    s[i] = c%mod

    ret = (ret + (c%mod)*i)%mod

print(ret)