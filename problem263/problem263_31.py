n = int(input())
a = list(map(int, input().split()))

mod = 10**9 + 7

pows = [pow(2, i, mod) for i in range(60)]
count = [0]*60
num = [0]*60
ans = 0

for i in range(n):
    bit = a[i]
    for g in range(60):
        if bit % 2 == 1:
            count[g] += 1
            num[g] += i+1 - count[g]
        else:
            num[g] += count[g]
        bit //= 2

for i in range(60):
    ans += num[i]*pows[i]

print(ans % mod)
