N, M = map(int, input().split())
s = []
c = []
for i in range(M):
    si, ci = map(int, input().split())
    s.append(si-1)
    c.append(ci)

answer = [-1] * N
valid = True
for i in range(M):
    if answer[s[i]] != -1 and answer[s[i]] != c[i]:
        valid = False
        break
    answer[s[i]] = c[i]

if answer[0] == 0 and N != 1:
    valid = False

if valid:
    if N == 1 and answer[0] == -1:
        answer[0] = 0
    elif answer[0] == -1:
        answer[0] = 1
    for i in range(N):
        if answer[i] == -1:
            answer[i] = 0
    print(int(''.join(map(lambda x: str(x), answer))))
else:
    print(-1)