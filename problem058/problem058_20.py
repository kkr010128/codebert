L = []
n,x = map(int, input().split())
while not(n == 0 and x == 0):
 L.append([n, x])
 n, x = map(int, input().split())

for i in L:
 ans = 0
 for j in range(1, i[0] - 1):
  if j > i[1] - 3:
   break
  else:
   for k in range(j + 1, i[0]):
    m = i[1] - (j + k)
    if m <= k:
     break
    elif m <= i[0]:
     ans += 1
    else:
     continue
 print(ans)