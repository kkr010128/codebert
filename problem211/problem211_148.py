n, r = map(int,input().split())

if n < 10:
  print(int(r+100*(10-n)))
elif n >= 10:
  print(r)