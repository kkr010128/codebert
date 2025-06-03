input_line = input().split()
n = int(input_line[0])
d = int(input_line[1])

count = 0
for i in range(n):
  c = input().split()
  x = int(c[0])
  y = int(c[1])
  if x**2 + y**2 <= d**2:
    count += 1

print(count)