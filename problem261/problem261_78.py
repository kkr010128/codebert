a = input()
b = a[::-1]
c = 0
for i in range(int(len(a)/2)):
  if a[i] != b[i]:
    c += 1
print(c)
