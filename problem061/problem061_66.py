s = input()
lc = s.lower()
uc = s.upper()

ans = ""
for i in range(len(s)):
    if s[i] == lc[i]:
        ans += uc[i]
    else:
        ans += lc[i]
print(ans)
