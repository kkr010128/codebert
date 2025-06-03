N = int(input())
A = list(input().split())
boss = [0]

for i in range(N-1):
  boss.append(0)
  boss[int(A[i])-1] += 1

for i in range(N):
  print(str(boss[i]))
