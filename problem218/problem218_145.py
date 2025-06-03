n = int(input())

d = {}

for i in range(n):
  a = input()
  if a not in d:
    d[a] = 1
  else:
    d[a] += 1

dsorted = sorted(d.items(), key=lambda x:x[1], reverse=True)

name = []
cnt = dsorted[0][1]

for i in dsorted:
  if i[1] == cnt:
    name.append(i[0])
  else:
    break

name.sort()

for i in name:
  print(i)