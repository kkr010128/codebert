N, K = map(int, input().split())
snuke = [False] * (N + 1)

for _ in range(K):
    d = int(input())
    A = list(map(int, input().split()))
    for a in A:
        snuke[a] = True

ans = 0
for i in range(1, N + 1):
    if snuke[i] == False:
        ans += 1

print(ans)
