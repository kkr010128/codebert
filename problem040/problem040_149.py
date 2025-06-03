a, b, c = map(int, raw_input().split())
temp = 0

if c < a:
  temp = c
  c = a
  a = temp
if c < b:
  temp = b
  b = c
  c = temp
if b < a:
  temp = a
  a = b
  b = temp

print '{0} {1} {2}'.format(a, b, c)