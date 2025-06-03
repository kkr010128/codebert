P = 10**9 + 7

K = int(input())
S = input()
L = len(S)

d = [0]*(L+K+1)
d[0] = 1
for i in range(1, L+K+1):
    d[i] = (d[i-1]*i)%P

ans = 0
for i in range(K+1):
    temp = pow(26, i, P) * pow(25, K-i, P)
    temp %= P
    temp *= d[L-1+K-i]
    temp %= P
    temp *= pow(d[L-1], P-2, P)
    temp %= P
    temp *= pow(d[K-i], P-2, P)
    temp %= P
    ans += temp
    ans %= P

print(ans)