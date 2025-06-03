n = int(input())

xmin = int(n/1.08)
xmax = int((n+1)/1.08)


if n%27 == 0:
  print(xmax)
elif (n+1)%27 == 0:
  print(":(")
elif xmin == xmax:
  print(":(")
else:
  print(xmax)