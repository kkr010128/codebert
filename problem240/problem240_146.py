n, m = map(int, input().split())
ps = [input().split() for i in range(m)]
b = [False] * n
wa = [0] * n
for i in ps:
  if b[int(i[0])-1] == False and i[1] == "AC":
    b[int(i[0])-1] = True
  elif b[int(i[0])-1] == False and i[1] == "WA":
    wa[int(i[0])-1] += 1
print(b.count(True),end=" ")
ans = 0
for i in range(n):
    if b[i]:
        ans += wa[i]
print(ans)        