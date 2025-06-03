nn = int(input())
number_of_match = [0 for _ in range(10005)]
for xx in range(1,105):
  xxxx = xx**2
  for yy in range(1,105):
    yyyy = yy**2
    xxyy = xx*yy
    for zz in range(1,105):
      result = xxxx + yyyy + (zz)**2 + xxyy + (yy)*(zz) + (zz)*(xx)
      if result < 10005:
        number_of_match[result] += 1
for i in range(1,nn+1):
  print(number_of_match[i])