N, K = map(int, input().split())

sunuke = [False] * N
for _ in range(K):
  d = int(input())
  A = list(map(int, input().split()))
  for a in A:
    a -= 1
    sunuke[a] = True

ans = N - sum(sunuke)
print(ans)
