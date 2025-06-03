N, K = map(int, input().split())
S = [i+1 for i in range(N)]
H = [0 for i in range(N)]
for i in range(K):
    d = int(input())
    A = list(map(int, input().split()))
    for j in A:
        for k in S:
            if j==k:
                H[k-1] += 1

ans = 0
for i in H:
    if i==0:
        ans += 1

print(ans)