N, K = map(int, input().split())
ans = []
for i in range(K):
    d = int(input())
    ans += map(int, input().split())
print(N-len(set(ans)))