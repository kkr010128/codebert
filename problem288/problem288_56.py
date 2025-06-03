n = int(input())

steps = []

for x in range(int(n ** 0.5)):
  if n % (x + 1) == 0:
    steps.append(x + n // (x + 1) - 1)
print(min(steps))
