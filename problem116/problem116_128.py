s = list(input())
t = list(input())
cnt = 0

for i in range(len(s)):
    if s[i] == t[i]:
        continue
    else:
        cnt += 1
print(cnt)