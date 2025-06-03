n = int(input())
r = s = 0
for i in range(n):
  a, b = input().split()
  if a > b:
    r += 3
  elif a < b:
    s += 3
  else:
    r += 1; s += 1
print(r,s)
