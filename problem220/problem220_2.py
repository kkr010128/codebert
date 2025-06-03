s,t = list(map(str,input().split()))
a,b = list(map(int,input().split()))
u = str(input())

if s == u:
  print(a - 1,b)
elif t == u:
  print(a,b - 1)