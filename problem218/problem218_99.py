n = int(input())
d = dict()

for i in range(n):
  s = input()
  if(s not in d.keys()):
    d[s] = 1
  else:
    d[s] +=1
    
max = max(d.values())
ans = []
for i in d.keys():
  if(d[i] == max):
    ans.append(i)
for i in sorted(ans):
  print(i)

