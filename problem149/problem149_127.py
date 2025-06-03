N, M, X = map(int, input().split())
Ca = [list(map(int, input().split())) for _ in range(N)]
pattern = []
for i in range(2**N):
    lis = []
    for j in range(N):
        if ((i>>j)&1):
            lis.append(Ca[j])
    pattern.append(lis)

cnt = []
for i in range(2**N):
    g = [0] * (M+1)
    for j in range(len(pattern[i])):
        for k in range(M+1):
            g[k] += pattern[i][j][k]
    if M==1 and g[1]< X:
        continue
    elif M>1 and min(g[1:M+1]) < X:
        continue
    else:
        cnt.append(g[0])
if len(cnt) ==0:
    print(-1)
else:
    print(min(cnt))