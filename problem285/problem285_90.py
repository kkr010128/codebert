s = input()
de_num = 0
le_num = 0
ans = [0]*(len(s)+1)

for i in range(len(s)):
    if s[i] == "<":
        de_num += 1
    else:
        de_num = 0
    ans[i+1] = de_num

s = s[::-1]
ans.reverse()

for i in range(len(s)):
    if s[i] == ">":
        le_num += 1
    else:
        le_num = 0
    ans[i+1] = max(le_num,ans[i+1])

print(sum(ans))