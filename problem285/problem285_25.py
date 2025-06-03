s = input()
n = len(s)
L=[0]
R=[0]
cnt = 0

for i in range(n):
    if s[i] == '<':
        cnt += 1
    else:
        cnt = 0
    L.append(cnt)
cnt = 0
s = s[::-1]
for i in range(n):
    if s[i]  == '>':
        cnt += 1
    else:
        cnt = 0
    R.append(cnt)

R = R[::-1]
ans = 0
for i in range(n+1):
    ans += max(R[i], L[i])

print(ans)