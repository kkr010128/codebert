n, m = map(int, input().split())
if m%2 == 1:
  for i in range(int((m-1)/2)):
    print(str(i+1) + ' ' + str(m-i))
  for i in range(int((m+1)/2)):
    print(str(m+i+1) + ' ' + str(2*m-i+1))
else:
  for i in range(int(m/2)):
    print(str(i+1) + ' ' + str(m-i+1))
  for i in range(int(m/2)):
    print(str(i+m+2) + ' ' + str(2*m-i+1))