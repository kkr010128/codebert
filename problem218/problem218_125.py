N = int(input())
dic = {}

for i in range (N):
  s = input()
  if s in dic:
    dic[s] += 1
  else:
    dic[s] = 1

sai = max(dic.values())

for j in sorted(k for k in dic if dic[k] == sai):
  print(j)