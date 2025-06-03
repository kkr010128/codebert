s = input()
t = input()

n = len(s) - len(t)
l = len(t)

res = 0
for i in range(n+1):
    cnt = 0
    for j in range(l):
        if s[i+j] == t[j]:
            cnt += 1
    res = max(res, cnt)

print(l - res)