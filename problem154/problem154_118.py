N, K = map(int, input().split())
cnts = [0] * N
for _ in range(K):
    di = int(input())
    A = list(map(int, input().split()))
    for i in range(di):
        cnts[A[i]-1] += 1

ans = cnts.count(0)
print(ans)