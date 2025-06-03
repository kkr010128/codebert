a, b = input().split()
c = a
a = a*int(b)

b = b*int(c)


for i in range(len(a)):
  if a[i]<b[i]:
    print(a)
    break
  elif a==b:
    print(a)
    break
  else:
    print(b)
    break
