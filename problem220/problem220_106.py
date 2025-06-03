a,b = input().split()
c,d = map(int,input().split())
e = input()

if a == e:
  print("{} {}".format(c-1,d))
else:
  print("{} {}".format(c,d-1))
