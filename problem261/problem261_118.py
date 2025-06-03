s = input()
t = list(reversed(s))
ans = 0
for i in range(len(s)):
    if s[i] != t[i]:
        ans += 1
ans = (ans+1) // 2
print(ans)