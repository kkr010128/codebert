N, M = map(int, input().split())
S = ['a'] * (N+1)
for i in range(M):
    s, c = list(map(int, input().split()))
    if S[s] != 'a' and S[s] != str(c):
        print(-1)
        exit()
    S[s] = str(c)
if S[1] == '0' and N > 1:
    print(-1)
    exit()
for i in range(1, N+1):
    if S[i] == 'a':
        if i == 1 and N > 1:
            S[i] = '1'
        else:
            S[i] = '0'
print(int(''.join(S[1:])))
