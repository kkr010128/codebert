from collections import defaultdict
N = int(input())
List = list(map(int,input().split()))
dicL = defaultdict(int)
dicR = defaultdict(int)
for i in range(N):
  dicL[List[i]+i] += 1
  dicR[i - List[i]] += 1
counter = 0
for item in dicL:
  if item in dicR:
    counter += dicL[item]*dicR[item]
print(counter)