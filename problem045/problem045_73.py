a,b = map(float, raw_input().split())

if b > 10**6:
  f = 0.0
else:
  f = a/b

d = int(a/b)
r = int(a%b)


print d, r, f 