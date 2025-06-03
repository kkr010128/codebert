s = input()
n = len(s)+1
ls = [0]*n
rs = [0]*n
for i in range(n-1):
    if s[i] == "<":
        ls[i+1] = ls[i]+1
for i in range(n-1):
    if s[-1-i] == ">":
        rs[-2-i] = rs[-1-i]+1
ans = 0
for i,j in zip(ls,rs):
    ans += max(i,j)
print(ans)