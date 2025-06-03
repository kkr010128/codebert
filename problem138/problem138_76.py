import sys
input = sys.stdin.readline

n, s = map(int,input().split())
A = list(map(int,input().split()))

mod = 998244353
l = 3050

M = [1]  # i!のmod
m = 1
for i in range(1, l):
    m = (m * i) % mod
    M.append(m)

def pow(x, y, mod):  # x**y の mod を返す関数
    ans = 1
    while y > 0:
        if y % 2 == 1:
            ans = (ans * x) % mod
        x = (x**2) % mod
        y //= 2
    return ans

def inv(x, mod):  # x の mod での逆元を返す関数
    return pow(x, mod-2, mod)

D = [0] * 3050

M2 = [1]
M2I = [0] * l

for i in range(l-1):
    M2.append((M2[-1] * 2) % mod)
for i in range(l):
    M2I[i] = inv(M2[i], mod)

i2 = inv(2,mod)

D[0] = M2[n]
for i in range(n):
    for j in range(l-1,-1,-1):
        if j - A[i] >= 0:
            D[j] = (D[j] + D[j-A[i]] * i2) % mod
    # print(D[:10])
    
print(D[s])

