x = map(int, input().replace(' ',''))
x = list(x)

for idx in range(len(x)):
  if x[idx] == 0:
    print(idx + 1)
    break