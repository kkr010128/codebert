N = int(input())
X = input()

a = X.count("1")
ap, am = a+1, a-1
Flag = True

if am == 0:
  Flag = False
  am += 1

Ap = [1]
Am = [1]

for i in range(N-1):
  Ap.append(Ap[-1]*2%ap)
  Am.append(Am[-1]*2%am)

Aps = 0
Ams = 0

for i in range(N):
  if X[-1-i] == "1":
    Aps += Ap[i]
    Aps %= ap
    Ams += Am[i]
    Ams %= am
    
def popcount(x):
    x = x - ((x >> 1) & 0x5555555555555555)
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f 
    x = x + (x >> 8) 
    x = x + (x >> 16)
    x = x + (x >> 32)
    return x & 0x0000007f

for i in range(N):
  cnt = 0
  if X[i] == "1":
    if Flag:
      p = Ams - Am[-1-i]
      p %= am
      cnt += 1
    else:
      p = 0
  else:
    p = Aps + Ap[-1-i]
    p %= ap
    cnt += 1
  while p > 0:
    p %= popcount(p)
    cnt += 1
  print(cnt)