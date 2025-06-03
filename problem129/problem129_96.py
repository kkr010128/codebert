n = int(input())
lst = [int(i) for i in input().split()]
lst.sort()
#print(lst)

if 1 in lst:
  count = 0
  for i in range(n):
    if lst[i] == 1:
      count += 1
    if count == 2:
      break
  if count == 1:
    print(1)
  else:
    print(0)
else:
  tf_lst = [1] * lst[n - 1]
  count = 0
  if n > 1:
    pre = 0
    for i in range(n):
      tf_lst[pre:lst[i] - 1] = [0] * (lst[i] - pre - 1)
      pre = lst[i]
      if tf_lst[lst[i] - 1] == 0:
        continue
      if i <= n - 2:
        if lst[i] == lst[i + 1]:
          tf_lst[lst[i] - 1] = 0
      for j in range(lst[i] * 2, lst[n - 1] + 1, lst[i]):
        tf_lst[j - 1] = 0
    #print(tf_lst)
    for i in tf_lst:
      count += i
  else:
    count += 1
  print(count)
