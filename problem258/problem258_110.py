n = int(input())

if n%2 == 1:
  print (0)
  exit()

cnt = 0
for i in range(1,26):
  x = pow(5,i)
  x *= 2
  if x > n:
    continue
  cnt += n//x
print (cnt)