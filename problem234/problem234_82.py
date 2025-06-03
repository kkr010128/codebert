N = int(input())
count = [0,1]
if N == 1:
  print(1)
  exit()
for i in range(2,N+1):
  digit = len(str(i))
  head = int(str(i)[0])
  tail = int(str(i)[-1])
  plus = 0
  if digit == 1:
    plus=1
  elif digit == 2:
    if head == tail:
      plus = 3
    elif head>tail and tail>0:
      plus = 2
  elif tail>0:
    for j in range(digit-2):
      plus += 10**j*2
    if head == tail:
      mid = str(i)[1:-1]
      while len(mid)>1 and mid[0]=='0':
        mid = mid[1:]
      mid = int(mid)
      plus += 2*mid+1
      plus += 2
    elif head > tail:
      plus += 10**(digit-2)*2
  count.append(count[-1]+plus)
print(count[N])
      
