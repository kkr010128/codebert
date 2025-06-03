n, p = map(int, input().split())

s = input()

ruisekiwa = [0 for _ in range(0, n + 1)]
if 10 % p == 0:
    ans = 0
    for i in range(0, n):
        if (ord(s[i]) - ord('0')) % p == 0:
            ans += i + 1
    print(ans)
    exit()

ten = 1
for _i in range(0, n):
    i = n - _i - 1
    ruisekiwa[n - i] = ((ord(s[i]) - ord('0')) * ten + ruisekiwa[n - i - 1]) % p
    ten *= 10
    ten %= p

ans = 0
cnt = [0 for _ in range(0, p)]
for i in range(0, n+1):
    ans += cnt[ruisekiwa[i]]
    cnt[ruisekiwa[i]] += 1

print(ans)
