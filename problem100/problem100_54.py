n = int(input())
if n >= 400 and n <= 599:
  kyu = 8
elif n >= 600 and n <= 799:
  kyu = 7
elif n >= 800 and n <= 999:
  kyu = 6
elif n >= 1000 and n <= 1199:
  kyu = 5
elif n >= 1200 and n <= 1399:
  kyu = 4
elif n >= 1400 and n <= 1599:
  kyu = 3
elif n >= 1600 and n <= 1799:
  kyu = 2
elif n >= 1800 and n <= 1999:
  kyu = 1
print(kyu)