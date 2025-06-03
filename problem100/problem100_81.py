X = int(input())
MIN = 400
MAX = MIN + 199
for i in range(8):
  if MIN <= X and X <= MAX:
    print(8 - i)
    break
  MIN = MIN + 200
  MAX = MIN + 199