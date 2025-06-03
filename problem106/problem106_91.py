import itertools
n = int(input())
dic = {}
for x in range(1, 101):
  for y in range(1, 101):
    for z in range(1, 101):
      f_xyz = x**2 + y**2 + z**2 + x*y + y*z + z*x
      if f_xyz in dic:
        dic[f_xyz] += 1
      else:
        dic[f_xyz] = 1
for i in range(1, n+1):
  if i in dic:
    print(dic[i])
  else:
    print(0)