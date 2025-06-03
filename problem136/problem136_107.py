n = int(input())

lst = []
while n % 2 == 0:
  lst.append(2)
  n //= 2
f = 3
while f * f <= n:
  if n % f == 0:
    lst.append(f)
    n //= f
  else:
    f += 2
if n != 1:
  lst.append(n)
#print(lst)
count = 0
while lst:
  s = 0
  i = 1
  num = lst[0]
  for ele in lst:
    if ele == num:
      s += 1
  for j in range(s):
    lst.remove(num)
  while s > 0:
    s -= i
    i += 1
    if s >= 0:
      count += 1
  #print(lst)
print(count)