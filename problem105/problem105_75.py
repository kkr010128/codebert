input()

result = 0
for i, x in enumerate([int(a) for a in input().split()]):
  result += (i+1) & 1 and x & 1
print(result)