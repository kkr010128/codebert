n = input().split()
a = int(n[0])
b = int(n[1])
c = int(n[2])
counta = 0
if a == b:
    if c % a == 0:
        counta += 1
else:
  for i in range(a,b+1):
      if c % i == 0:
          counta += 1
print(counta)