i = input()
a,b,c = map(int, i.split())

s = set()

s.add(a)
s.add(b)
s.add(c)

if len(s) == 2: 
  print("Yes")
else:
  print("No")