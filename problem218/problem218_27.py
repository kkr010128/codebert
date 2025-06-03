n = int(input())
S = ['']*n
T = []
for i in range(n):
    S[i] = input()
S.sort()
if n == 1:
    print(S[0])
    exit()
cnt = 1
mxcnt = 1
for i in range(n-1):
    if S[i] == S[i+1]:
        cnt += 1
    else:
        cnt = 1
    mxcnt = max(mxcnt,cnt)
cnt = 1
for i in range(n-1):
    if S[i] == S[i+1]:
        cnt += 1
    else:
        cnt = 1
    if cnt == mxcnt:
        T.append(S[i])
if mxcnt == 1:
    T.append(S[-1])
for t in T:
    print(t)