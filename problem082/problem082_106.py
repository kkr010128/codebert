s = input()
t = input()
ss = len(s)
tt = len(t)
min = tt


for i in range(ss - tt + 1):
  count = 0
  for j in range(tt):
    if s[i+j] != t[j]:
      count += 1
  if min > count:
    min = count

print(min) 
