s = input()
t = input()

ans = "Yes"
for i in range(len(s)):
    if s[i] == t[i]:
        continue
    else:
        ans = "No"
if ans == "Yes" and (len(s)+1) == len(t):
    ans = "Yes"
else:
    ans = "No"

print(ans)