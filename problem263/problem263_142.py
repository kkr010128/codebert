n = int(input())
a = list(map(int,input().split()))
mod = 10**9 + 7

c = [n]*61
for i in range(n):
    b = str(bin(a[i]))[2:]
    b = b[::-1]
    for j, x in enumerate(b):
        if x == "1":
            c[j] -= 1

ans = 0
for i in range(60):
    ans += c[i]*(n-c[i])*pow(2,i,mod)
    ans %= mod
print(ans)
