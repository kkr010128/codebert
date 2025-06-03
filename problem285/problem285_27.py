s = input()
ans = chk = 0
ans = [-1] * (len(s)+1)
if s[0] == "<":
    ans[0] = 0
if s[-1] == ">":
    ans[-1] = 0
for i in range(len(s) - 1):
    if s[i] == ">" and s[i+1] == "<":
        ans[i+1] = 0
for i in range(len(s)):
    if s[i] == "<":
        ans[i+1] = ans[i] + 1
for i in range(-1, -len(s)-1,-1):
    if s[i] == ">":
        ans[i-1] = max(ans[i-1], ans[i]+1)
print(sum(ans))
