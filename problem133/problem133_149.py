def multiply(values):
  out = 1
  for i in values:
    out *= int(i)
  print(out)

stdin = input().split()
multiply(stdin)