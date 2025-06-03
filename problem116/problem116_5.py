n_s = list(input().rstrip())
n_t = list(input().rstrip())
cnt = 0
for i in range(len(n_s)):
    if n_s[i] != n_t[i]:
        cnt += 1
print(cnt)