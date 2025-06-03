w = input()
l = len(w)
flag = True
for i in range((l - 1)//2):
  if w[i] != w[l - i - 1]:
    flag = False
    break
mid = (l - 1) // 2
mid_mid = mid // 2
for i in range(mid_mid + 1):
  if w[i] != w[mid - i - 1] or not flag:
    flag = False
    break
  if w[i + mid + 1] != w[l - i - 1]:
    flag = False
    break
if flag:
  print('Yes')
else:
  print('No')
