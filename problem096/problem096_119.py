N, D = map(int, input().split())
D = D*D
count = 0
for i in range(N):
  P = list(map(int, input().split()))
  dis = P[0]*P[0] + P[1]*P[1]
  if dis <= D:
    count += 1
print(count)
