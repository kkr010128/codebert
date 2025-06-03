x = int(input())

for i1 in range(x//105, -1, -1):
  x2 = x - 105*i1
  for i2 in range(x2//104, -1, -1):
    x3 = x2 - 104*i2
    for i3 in range(x3//103, -1, -1):
      x4 = x3 - 103*i3
      for i4 in range(x4//102, -1, -1):
        x5 = x4 - 102*i4
        for i5 in range(x5//101, -1, -1):
          x6 = x5 -101*i5
          for i6 in range(x6//100, -1, -1):
            if x5 - 100*i6 == 0:
              print(1)
              exit()
print(0)