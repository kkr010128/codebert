N, K = map(int, input().split())
P = list(map(int, input().split()))
ans = sum(sorted(P)[:K])
print(ans)