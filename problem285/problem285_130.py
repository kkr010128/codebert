s = input()
d = [[0]*2 for _ in range(len(s)+1)]
count_r = 0
count_l = 0
ans = 0
for i in range(len(s)):
    if s[i] == "<":
        d[i+1][0] = d[i][0]+1
    else:
        d[i+1][0] = 0
for i in range(len(s)-1, -1, -1):
    if s[i] == ">":
        d[i][1] = d[i+1][1]+1
    else:
        d[i][1] = 0
for i in range(len(s)+1):
    ans += max(d[i])
print(ans)