S = int(input())

if S < 3:
  print(0)
  import sys
  sys.exit()

DP = [0]*(S+1)
DP[0] = 0
DP[1] = 0
DP[2] = 0

for i in range(3, S + 1):
  DP[i] += 1
  for j in range(i - 3 + 1):
    DP[i] += DP[j]

print(DP[S] % (10 ** 9 + 7))
