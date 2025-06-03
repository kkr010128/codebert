X = int(input())
flag = 1
if X < 100:
  flag = 0
else:
  a = X%100
  b = a%10
  c = (a-b)/10
  count = 2*c
  if 1 <= b <= 5:
    count += 1
  elif 6<= b <= 9:
    count += 2
  if X//100 < count:
    flag = 0
print(flag)