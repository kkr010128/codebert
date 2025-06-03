S = input()

N = len(S)
num = 0
L = [0]
R = [0]
cnt = 0

for i in range(N):
    if S[i] == "<":
        cnt += 1
    else:
        cnt = 0
    L.append(cnt)

ans = 0
S = S[::-1]
cnt = 0

for i in range(N):
    if S[i] == ">":
        cnt += 1
    else:
        cnt = 0
    R.append(cnt)

R = R[::-1]

for i in range(N+1):
    ans += max(L[i], R[i])

print(ans)
