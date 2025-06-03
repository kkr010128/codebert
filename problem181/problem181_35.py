N = int(input())
if N <= 9:
  print(N)
  exit()
A = [[] for _ in range(11)]
A[0] = [1,2,3,4,5,6,7,8,9]
now = 9
keta = 1
while True:
  for x in A[keta-1]:
    x = str(x)
    last = int(x[-1])
    if last - 1 >= 0:
      temp = x+str(last-1)
      A[keta].append(int(temp))
      now += 1
      if now == N:
        print(temp)
        exit()
    temp = x+str(last)
    A[keta].append(int(temp))
    now += 1
    if now == N:
      print(temp)
      exit()
    if last+1 <= 9:
      temp = x+str(last+1)
      A[keta].append(int(temp))
      now += 1
      if now == N:
        print(temp)
        exit()
  keta += 1

