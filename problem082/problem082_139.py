s = input()
t = input()
ans = 1001001001
for i in range(len(s) - len(t) + 1):
    cnt = 0
    for j in range(len(t)):
        if s[i + j] != t[j]:
            cnt += 1
    if cnt <= ans:
        ans = cnt
print(ans)
