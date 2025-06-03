N,K = map(int,input().split())
have = [0] * N
for i in range(K):
    d = int(input())
    As = list(map(int,input().split()))
    for j in range(d):
        have[As[j]-1] += 1

ans = 0
for i in range(N):
    if have[i] == 0:
        ans += 1
print(ans)
