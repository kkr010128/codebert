n=int(input())

result = [0] * (n+1)
for x in range(1,99):
  for y in range(1,99):
    for z in range(1,99):
      fn = x*x + y*y + z*z + x*y + y*z + z*x
      if fn > n:
        break
      result[fn] += 1

for i in range(1,n+1):
  print(result[i])
