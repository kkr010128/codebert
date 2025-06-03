d = int(input())
c = [0] + list(map(int, input().split()))

s = [0]
for i in range(d):
  s.append([0] + list(map(int, input().split())))
  
t = [0]
for i in range(d):
  t.append(int(input()))
  
sati = [0] * (d+1)
last = [0] * 27

for i in range(1, d+1):
  sati[i] = sati[i-1] + s[i][t[i]]
  unsati = 0
  last[t[i]] = i
  for j in range(1, 27):
    unsati += c[j] * (i - last[j])
  sati[i] -= unsati
  
for i in range(1, d+1):
  print(sati[i])