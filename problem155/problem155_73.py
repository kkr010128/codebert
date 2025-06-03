N, M = list(map(lambda x: int(x), input().split(" ")))
H = list(map(lambda h: int(h), input().split(" ")))

dest = [[] for i in range(N)]
for i in range(M):
  tmp = input().split(" ")
  dest[int(tmp[0]) - 1].append(int(tmp[1]) - 1)
  dest[int(tmp[1]) - 1].append(int(tmp[0]) - 1)

good = 0
for i in range(len(dest)):
  d = dest[i]
  if len(list(filter(lambda j: H[i] - H[j] <= 0, d))) == 0:
    good += 1

print(good)