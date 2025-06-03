import copy

H, W, K = map(int, input().split())
inputdata = [list(str(input())) for i in range(H)]
data = []
temp = []
give = 0

for x in inputdata:
  data.append(list(x))

for i in range(2 ** H):
  for j in range(2 ** W):
    ans = 0
    temp = copy.deepcopy(data)
    for m in range(H):
      for n in range(W):
        if ((int(bin(i)[2:]) >> m) & 1) or ((int(bin(j)[2:]) >> n) & 1):
          temp[m][n] = "@"
        if temp[m][n] == "#":
          ans += 1
    if ans == K:
      give += 1

print(give)