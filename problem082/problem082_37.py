s = str(input())
t = str(input())

ans = len(t)
for i in range(len(s) - len(t) + 1):
    tmp_ans = 0
    for j in range(len(t)):
        if s[i+j] != t[j]:
            tmp_ans += 1
    ans = min(ans, tmp_ans)
print(ans)