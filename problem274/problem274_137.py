n, m = list(map(int, input().split()))
s = input()

if s.find('1' * m) != -1:
  print('-1')
  exit(0)

i = n
rans = []
flag = True
while flag:
  for j in range(m, 1 - 1, -1):
    if i - j == 0:
      flag = False
    if i - j >= 0 and s[i - j] == '0':
      rans.append(j)
      i = i - j
      break
  
print(' '.join(map(str,reversed(rans))))
