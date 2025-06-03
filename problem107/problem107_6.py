N = int(input())
X = str(input())
count = X.count("1")
num, nump, numm = 0, 0, 0
now, nowp, nowm = 1, 1, 1

if count == 0:
  for i in range(N):
    print(1)
    quit()
elif count == 1:
  if X[-1] == "1":
    for i in range(N):
      if i != N - 1:
        print(2)
      else:
        print(0)
  else:
    for i in range(N):
      if i!= N - 1:
        if X[i] == "1":
          print(0)
        else:
          print(1)
      else:
        print(2)
  quit()
  

xx = [0] * N
x_plus = [0] * N
x_minus = [0] * N
for i in range(1, N + 1):
  if i != 1:
    now *= 2
    nowp *= 2
    
    now %= count
    nowp %= (count + 1)
    

    nowm *= 2
    nowm %= (count - 1)
  
  else:
    now %= count
    nowp %= (count + 1)
    nowm %= (count - 1) 
  xx[i - 1] = now
  x_plus[i - 1] = nowp
  x_minus[i - 1] = nowm
  if X[-i] == "1":
    num += now
    num %= count
    nump += nowp
    nump %= count + 1
    numm += nowm
    numm %= count - 1
    
#print(num, xx, x_plus, x_minus)    

nextn = [0] * N
#ans = [1] * N
for i in range(N):
    if X[i] == "0":
      a = nump + x_plus[N - 1 - i]
      b = count + 1
      #print(a, b)
      nextn[i] = a % b
    else:
      #if count == 2:
      #  nextn[i] = 0
      #else:
        a = numm - x_minus[N - 1 - i]
        b = count - 1
        nextn[i] = a % b
        
#print(nextn)    
for i in range(N):
  if nextn[i] == 0:
    print("1")
  else:
    nownow = nextn[i]
    ans = 1
    while nownow != 0:
      alpha = bin(nownow)[2:]
      beta = str(alpha).count("1")
      nownow %= beta
      ans += 1
    print(ans)





