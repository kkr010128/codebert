N = int(input())
A = list(map(int, input().split()))
cnt = [0] * (100001)
ans = sum(A)
for a in A:
  cnt[a] += 1
Q = int(input())
for _ in range(Q):
  B, C = map(int, input().split())
  cnt[C] += cnt[B]
  ans += cnt[B] * (C-B)
  cnt[B] = 0
  print(ans)