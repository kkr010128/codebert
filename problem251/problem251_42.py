N, K = map(int, input().split())
SC = list(map(int, input().split()))
T = input()
Q = []
for i in range(len(T)):
  if T[i] == "r":
    Q.append(0)
  elif T[i] == "s":
    Q.append(1)
  else:
    Q.append(2)
my = [0 for i in range(N)]
ans = 0
for i in range(N):
  if i < K:
    my[i] = (Q[i] - 1) % 3
    ans += SC[my[i]]
  else:
    n = (Q[i] - 1) % 3
    if my[i - K] != n:
      my[i] = n
      ans += SC[my[i]]
    else:
      if i + K < N:
        my[i] = Q[i+K]
print(ans)