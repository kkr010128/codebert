s = input()
t = input()

ans = len(t)
for i in range(len(s) - len(t) + 1):
    tmp = s[i:i+len(t)]
    count = 0
    for t1, t2 in zip(tmp, t):
        if t1 != t2:
            count += 1
    ans = min(ans, count)
print(ans)
