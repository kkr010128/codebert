D = int(input())
c = [int(i) for i in input().split()]
s = []
for i in range(D):
  tmp = [int(j) for j in input().split()]
  s.append(tmp)
t = []
for i in range(D):
  t.append(int(input()))
  
sat = 0
lst = [0 for i in range(26)]

for i in range(D):
  sat += s[i][t[i]-1]
  lst[t[i]-1] = i + 1
  for j in range(26):
    sat -= c[j] * ((i + 1) - lst[j])
  print(sat)