from collections import Counter

n, p = map(int, input().split())
s = input()

ans = 0

if p in {2, 5}:
    lst = set(i for i in range(0, 10, p))
    for i, num in enumerate(s):
        if int(num) in lst:
            ans += i + 1
else:
    num = [0]
    for i in range(len(s)):
        tmp = num[-1] + pow(10, i, p) * int(s[-i - 1])
        num.append(tmp % p)
    mod = [0] * p
    for i in num:
        ans += mod[i]
        mod[i] += 1
print(ans)
