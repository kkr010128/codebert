N = int(input())
A = list(map(int, input().split()))
Q = int(input())
cnt = [0]*(10**5+1)

s = sum(A)
for i in A:
  cnt[i] += 1

for _ in range(Q):
  B, C = map(int, input().split())
  s += (C-B)*cnt[B]
  print(s)
  cnt[C] += cnt[B]
  cnt[B] = 0