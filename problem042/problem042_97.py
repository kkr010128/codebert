index = 0
inputs = []
while True:
  index += 1
  x = input()
  if x == '0':
    break
  else:
    inputs.append("Case {}: {}".format(index, x))
print("\n".join(inputs))