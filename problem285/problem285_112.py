s = input()
ans = [0 for i in range(len(s)+1)]

for i in range(len(s)):
    if s[i] == '<':
        ans[i+1] = max(ans[i+1],ans[i]+1)
for i in range(len(s)-1,-1,-1):
    if s[i] == '>':
        ans[i] = max(ans[i],ans[i+1]+1)

print(sum(ans))
