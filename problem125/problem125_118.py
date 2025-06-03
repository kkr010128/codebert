# A - Takahashikun, The Strider
x = int(input())
i = 1

while True:
  if 360 * i % x == 0:
    print(360 * i // x)
    break
  else:
    i += 1