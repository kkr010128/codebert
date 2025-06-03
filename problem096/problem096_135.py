import math

N, D = [int(x) for x in input().split()]

Z = []
for i in range(N):
  Z.append([int(x) for x in input().split()])


ans = 0
for i in range(N):
    if math.sqrt(Z[i][0]**2 + Z[i][1]**2) <= D:
        ans += 1


print(ans)
