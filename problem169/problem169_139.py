N = int(input())
A = list(map(int, input().split()))
bosses = [0 for _ in range(N+1)]
for boss in A:
  bosses[boss] += 1
for i in range(1, N+1):
  print(bosses[i])