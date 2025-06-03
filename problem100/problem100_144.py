x = int(input())

if x >= 1800:
  out = 1
elif x >= 1600:
  out = 2
elif x >= 1400:
  out = 3
elif x >= 1200:
  out = 4
elif x >= 1000:
  out = 5
elif x >= 800:
  out = 6
elif x >= 600:
  out = 7
else:
  out = 8

print(out)