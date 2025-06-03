def chk(x):
    cur = 0
    cnt = 0
    while cur<N:
        if S[cur]==str(x[cnt]):
            cnt += 1
            if cnt==3:
                break
        cur += 1
    if cnt==3:
        return 1
    else:
        return 0

N = int(input())
S = input().strip()
cnt = 0
for i in range(0,10):
    for j in range(0,10):
        for k in range(0,10):
            cnt += chk((i,j,k))
print(cnt)