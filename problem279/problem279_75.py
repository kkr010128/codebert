N = int(input())

q = input()
a = list(q)

if N % 2 == 1:
  print('No')
  
elif N % 2 == 0:
  b = [a] * int(N/2)
  c = [a] * int(N/2)
  for i in range(int(N/2)):
    b[i] = a[i]
  for j in range(int(N/2)):
    c[j] = a[int(j)+int(N/2)]
  if b == c:
    print('Yes')
  else:
    print('No')