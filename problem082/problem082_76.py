s = input()
t = input()
ls = len(s)
lt = len(t)
min_count = 1000
for i in range(ls-lt+1):
  count = 0
  for j in range(lt):
    if s[i:i+lt][j] != t[j]:
      count += 1
  if min_count > count:
    min_count = count
print(min_count)
