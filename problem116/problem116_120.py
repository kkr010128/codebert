a = input()
b = input()

res = 0

for i, char in enumerate(a):
  if char != b[i]:
    res += 1

print(res)