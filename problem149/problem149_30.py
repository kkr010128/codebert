N , M , X = list(map(int, input().split()))
C = []
for _ in range(N):
    C.append(list(map(int, input().split())))
ans = 10**9
for i in range(2**N):
    i_bin = (bin(i)[2:]).zfill(N)
    flag = True
    for j in range(1,M+1):
        tot = sum([ int(i_bin[k])* C[k][j] for k in range(N)])
        if tot < X:
            flag = False
    am = sum([ int(i_bin[k]) * C[k][0] for k in range(N)])
    if flag and am<ans:
        ans = am

if ans == 10**9:
    print(-1)
else:
    print(ans)