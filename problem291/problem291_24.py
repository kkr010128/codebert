i = list(map(int, input().split()))
o = i[0] - 2 * i[1]
if o <= 0:
  o = 0
print(o)