s = list(input())
t = list(input())

lt = len(t)
ans = lt

for i in range(len(s) - lt + 1):
    s_ = s[i: i + lt]
    diff = 0
    for x, y in zip(s_, t):
        if x != y:
            diff += 1
    ans = min(ans, diff)
print(ans)