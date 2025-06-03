s = list(input())

ans = 0
a = 0
for i in range(len(s)):
    if s[i] == 'R':
        a += 1
    else:
        a = 0
    ans = max(ans,a)

print(ans)