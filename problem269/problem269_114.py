import sys

t1, t2 = map(int, input().split())
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())

a = a1 * t1 + a2 * t2
b = b1 * t1 + b2 * t2
ha = a1 * t1
hb = b1 * t1
if a == b or ha == hb:
  print ("infinity")
  sys.exit(0)

if a > b:
  a, b = b, a
  ha, hb = hb, ha

gap = b - a
hgap = ha - hb

if hgap < 0:
  print (0)
  sys.exit(0)

ans = 2 * (hgap // gap) + (1 if hgap % gap > 0 else 0)
print (ans)


