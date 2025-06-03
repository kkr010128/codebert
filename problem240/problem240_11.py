n, m = map(int, input().split())
account, wacount = 0, 0
acdic = [0] * (n + 10)
for _ in range(m):
    p, s = input().split()
    p = int(p)
    if s == "AC" and acdic[p] <= 0:
        account += 1
        wacount += abs(acdic[p])
        acdic[p] = 1
    elif s == "WA" and acdic[p] <= 0:
        acdic[p] -= 1
print(account, wacount)