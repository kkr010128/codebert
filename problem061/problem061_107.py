s = raw_input()
ans = ""
for i in range(len(s)):
    if('A' <= s[i] and s[i] <= 'Z'):
        ans += s[i].lower()
    elif('a' <= s[i] and s[i] <= 'z'):
        ans += s[i].upper()
    else:
        ans += s[i]
print(ans)