n = int(input())
lst = [int(i) for i in input().split()]
dic = {}
for i in range(n):
  if lst[i] not in dic:
    dic[lst[i]] = [1, 0, 0]
  else:
    dic[lst[i]][0] += 1
    dic[lst[i]][1] = dic[lst[i]][0] * (dic[lst[i]][0] - 1) // 2
    dic[lst[i]][2] = (dic[lst[i]][0] - 1) * (dic[lst[i]][0] - 2) // 2
#print(dic)
count = 0
for value in dic.values():
  count += value[1]
for i in range(n):
  m = lst[i]
  count -= dic[m][1]
  count += dic[m][2]
  print(count)
  count += dic[m][1]
  count -= dic[m][2]