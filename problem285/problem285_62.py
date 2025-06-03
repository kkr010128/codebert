s = input()

x = 0
l = [0] * len(s)
for i in range(len(s)):
    if s[i] == "<":
        x += 1
        l[i] = x
    else:
        x = 0

x = 0
r = [0] * len(s)
for i in range(len(s))[::-1]:
    if s[i] == ">":
        x += 1
        r[i] = x
    else:
        x = 0

ans = l[-1] + r[0]
for i in range(len(s)-1):
    ans += max(l[i], r[i+1])
    
print(ans)