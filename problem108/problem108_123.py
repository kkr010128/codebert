s = int(input())
if s%1000 == 0:
  c=0
else:
  c = 1000 - ( s%1000 )
print(c)
