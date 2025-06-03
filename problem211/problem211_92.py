x = input().split()
n = int(x[0])
r = int(x[1])

if n >= 10:
  pass
else:
  r = r + 100 *(10-n)
  
print(r)