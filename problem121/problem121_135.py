from math import ceil

n = int(input())

a = [chr(i) for i in range(97, 97+26)]

s = 0
for i in range(1,100):
  l = n - s
  s += 26**i
  if n <= s:
    m = i
    break #第m群l番目

name = [0] * m
div = [0] * m
rem = [0] * m
rem[-1] = l

for j in range(m):
  div[j] = ceil(rem[j-1] / (26**(m-j-1)))
  rem[j] = rem[j-1] % (26**(m-j-1))
  if rem[j] == 0:
    rem[j] == 26**(m-j-1)
  name[j] = a[div[j]-1]
    
print(''.join(name))