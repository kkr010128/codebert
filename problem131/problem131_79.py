a, v = list(map(int, input().split(' ')))
b, w = list(map(int, input().split(' ')))
time = int(input())
if a>b:
  x1 = a - v*time
  x2 = b - w*time
  if x1 <= x2:
    print('YES')
  else:
    print('NO')
elif a<b:
  x1 = a + v*time
  x2 = b + w*time
  if x1 >= x2:
    print('YES')
  else:
    print('NO')
  


