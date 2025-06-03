N, M = map(int,input().split())
li = []
for _ in range(M):
  p, S = input().split()
  li.append([int(p), S])

ac = [0] * N
wa = [0] * N
c1 = 0
c2 = 0

for i in range(M):
  j = li[i][0] - 1
  if li[i][1] == "WA":
    wa[j] += 1
  if ac[j] == 0 and li[i][1] == "AC":
    ac[j] = 1
    c1 += 1
    c2 += wa[j]

print(c1, c2)
