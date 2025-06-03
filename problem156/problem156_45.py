from math import sqrt
x = int(input())

ps = []
for i in range(1, int(sqrt(x)) + 1):
  if x % i == 0:
    ps.append(i)
    ps.append(x // i)

for p_ in ps:
  for p in (-p_, p_):
    for r in (-1, 1):
      for s in (-1, 1):
        try:
            a = (p + r * sqrt(-5 * p**2 + s * (2 * sqrt(5) *
                                              sqrt(p ** 6 + 4 * p * x)) / p) / sqrt(5)) / 2
            if abs(a - round(a)) < 1e-6:
              a = round(a)
              print(a, a - p)
              exit()
        except ValueError:
          pass
