N = int(input())
S = str(input())
X = [];Bit = 0;Num = 0
for i in range(N):
  if S[i] == "1":
    Bit += 1
    Num += pow(2,N-1-i)
  X.append(int(S[i]))
#print(X)
#print(Num)
MAX = 2*pow(10,5)+10
small = [-1 for _ in range(MAX)]
small[0] = 0; small[1] = 1; small[2] = 1; small[3] = 2
for i in range(4,MAX):
  ret = 0; target = i*1
  while i > 0:
    cnt = 0
    for j in range(i.bit_length()):
      if (i>>j)&1 == 1:
        cnt += 1
    i = i%cnt
    #print(i,target,cnt)
    ret += 1
    if small[i] != -1:
      ret += small[i]
      break

  small[target] = ret
#print(small)
if Bit -1 != 0:
  Numm = Num%(Bit-1)
Nump = Num%(Bit+1)
#print(Num)
ans = []
for i in range(N):
  keta = N-1-i
  if X[i] == 1:
    btemp = Bit -1
    if btemp == 0:
      ans.append(0)
      continue
    temp = (Numm - pow(2,keta,btemp))%btemp
  else:
    btemp = Bit +1
    temp = (Nump + pow(2,keta,btemp))%btemp
  ret = small[temp] + 1 #最初の一回
  ans.append(ret)
print(*ans,sep="\n")