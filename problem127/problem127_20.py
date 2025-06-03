x, y = map(int, input().split())
a = []
for i in range(0, x+1):
  a.append(2 * i + 4 * (x - i))
print("Yes" if y in a else "No")