l = []
while True:
  s = [int(i) for i in input().split()]
  if s == [0,0]:
    break
  else:
    s.sort()
    l.append(str(s[0])+' '+str(s[1]))
for i in l:
  print(i)