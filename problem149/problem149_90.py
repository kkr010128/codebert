N,M,X = map(int,input().split())
data = []
ans = 0
for i in range(N):
    d = list(map(int,input().split()))
    data.append(d)
    ans += d[0]

x = 2**N + 1
ans_candidate = []
valid = False
ans += 1
ans_old = ans
for i in range(x):
    if i != 0:
        for l in range(len(sum)):
            if sum[l] >= X and l == len(sum) -1:
                valid = True
            if sum[l] >= X:
                continue
            else:
                valid = False
                break
        if valid and price < ans:
            ans = price
    sum = [0] * M
    price = 0
    for j in range(N):
        if i >> j & 1 == 1:
            price += data[j][0]
            for k in range(M):
                sum[k] += data[j][k+1]

if ans_old == ans:
    print(-1)
else:
    print(ans)
