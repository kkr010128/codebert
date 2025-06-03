n,r = input().split()
n = int(n)
r = int(r)

if n >= 10:
  i = r
else:
  i = r + 100 * (10 - n)
print(i)