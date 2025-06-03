N, K = map(int, input().split())
d = [0]*K
A = []
for i in range(K):
    d[i] = int(input())
    A.append(list(map(int, input().split())))
ans = 0
for i in range(1,N+1):
    got = False
    for j in A:
        for k in j:
            if i == k:
                got = True
    if not got:
        ans += 1
print(ans)