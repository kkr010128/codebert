k = int(input())

ok = False
for i in range(1, k+1):
   if i == 1:
      a = 7 % k
   else:
      anext = (a * 10 + 7) % k
      a = anext
   if a == 0:
      print(i)
      ok = True
      break

if not ok:
   print(-1)
