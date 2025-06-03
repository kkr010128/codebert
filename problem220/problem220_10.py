s = input().split()
a, b = map(int, input().split())
t = input()
if s[0] == t:
  print(str(a-1) + " " + str(b))
else:
  print(str(a) + " " + str(b-1))
