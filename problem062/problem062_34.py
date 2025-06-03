n = int(input())
res = 0
while n != 0:
 res = n%10
 dropped = n
 while dropped//10 != 0:
  dropped = dropped//10
  res += dropped%10
 print(res)
 res = 0
 n = int(input())