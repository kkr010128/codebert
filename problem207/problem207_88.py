A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
A3 = list(map(int, input().split()))
N = int(input())
B = [int(input()) for i in range(N)]
result = ''

for b in B:
  if b in A1:
    a = A1.index(b)
    A1.remove(b)
    A1.insert(a, 0)
  elif b in A2:
    a = A2.index(b)
    A2.remove(b)
    A2.insert(a, 0)
  elif b in A3:
    a = A3.index(b)
    A3.remove(b)
    A3.insert(a, 0)
  else:
    pass


if A1.count(0) == 3:
  result ='y'
elif A2.count(0) == 3:
  result ='y'
elif A3.count(0) == 3:
  result ='y'

for m in range(3):
  if A1[m] == 0 and A2[m] == 0 and A3[m] == 0:
    result ='y' 
  else:
    pass


if A1[0] == 0 and A2[1] == 0 and A3[2] == 0:
  result = 'y'
elif A1[2] == 0 and A2[1] == 0 and A3[0] == 0:
  result = 'y'


if result == 'y':
  print('Yes')
else:
  print('No')

