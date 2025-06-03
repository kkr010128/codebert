a,b,c = map(int, input().split())

t = [a,b,c]
t.sort()

if (t[0] == t[1] and t[1] != t[2]) or (t[0] != t[1] and t[1] == t[2]):
  print("Yes")
else:
  print("No")