NK = list(map(int, input().split()))
P = list(map(int, input().split()))
sum = 0
P.sort()

for i in range(NK[1]):
  sum+=P[i]

print(sum)