x = input()
a = x[::-1]
b = 0
c = 0
d = int(len(x))
while b + 1 <= d:
  if x[b] == a[b]:
    c = c
    b = b + 1
  else:
    c = c + 1
    b = b + 1
c = int(c/2)
print(c)