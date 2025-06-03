n = int(input())
s = [input() for _ in range(n)]
 
d = {}
for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
        
m = max(d.values())

l = []
for i in d.keys():
  if d[i] == m:
  	l.append(i)
    
l_s = sorted(l)
for i in l_s:
  print(i)