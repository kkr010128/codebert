import collections

N = int(input())
hList = list(map(int, input().split()))
count = 0
n_p = collections.Counter([ i + hList[i] for i in range(len(hList))])

for i in range(N):
  if i - hList[i] > 0:
    count += n_p.get(i - hList[i], 0)

print(count)