N, M = map(int, input().split())
S = []
C = []
for _ in range(M):
    s, c = map(int, input().split())
    S.append(s)
    C.append(c)
    

n = int('9'*N)
if N > 1:
    start = int('1' + '0'*(N-1))
else:
    start = 0
ans = []

for i in range(start, n+1):
    I = str(i)
    for m in range(M):
        if N >= 2 and S[m] == 1 and C[m] == 0:
            break
        if S[m] <= len(I):
            if I[S[m]-1] != str(C[m]):
                break
    else:
        ans.append(I)

if len(ans) == 0:
    print(-1)
    exit()

ans_map = list(map(int,ans))

print(min(ans_map))
