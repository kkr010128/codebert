import itertools

N = int(input())
cities = [list(map(int, input().split())) for _ in range(N)]
patterns = itertools.permutations(cities, N)
result = 0
count = 0
for ptn in patterns:
  count += 1
  dis = 0
  for i in range(N-1):
    dis += ((ptn[i][0]-ptn[i+1][0])**2 + (ptn[i][1]-ptn[i+1][1])**2)**0.5
  result += dis
print(result/count)

