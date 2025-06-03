s = input()
t = input()

ls = len(s)
lt = len(t)
ret = lt
for i in range(ls+1 - lt):
  diff = 0
  for j in range(lt):
    diff += (t[j] != s[i+j])
  if diff == 0:
    ret = diff
    break
  if diff < ret:
    ret = diff
print(ret)