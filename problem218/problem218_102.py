N = int(input())
d = dict()
for i in range(N):
  let = input()
  if let in d:
    d[let] += 1
  else:
    d[let] = 0
max = 0
res = []
for i in d:
  if d[i]  > max:
    max = d[i]
    res =[i]
  elif d[i] == max:
    res.append(i)
for i in sorted(res):
  print(i)