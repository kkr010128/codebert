import math
import bisect
MOD = 1000000007

N = int(input())
ABs =  []

count00 = 0
for i in range(N):
  A, B = map(int, input().split())
  if A == 0:
    if B == 0:
      count00 += 1
    else:
      ABs.append([0, -1])
  elif B == 0:
    ABs.append([1, 0])
  else:
    mygcd = math.gcd(A, B)
    A, B = A//mygcd, B//mygcd
    if A < 0:
      ABs.append([-A, -B])
    else:
      ABs.append([A, B])
  
N2 = N - count00
if N2 == 0:
  print(count00)
  exit()

ABs.sort(key = lambda x:x[1])
Bs = [i[1] for i in ABs]
index0 = bisect.bisect_left(Bs, 0)

if (index0==0) or (index0==N2):
  print((pow(2, N2, MOD) +count00 -1) %MOD)
  exit()

btm = ABs[:index0]
top = ABs[index0:]

lenbtm = index0
lentop = N2 - index0
for i in range(lenbtm):
  btm[i] = [-btm[i][1], btm[i][0]]

btmdict = {}
topdict = {}
for i in btm:
  mykey = str(i[0]) + '-' + str(i[1])
  btmdict[mykey] = 0
  topdict[mykey] = 0
for j in top:
  mykey = str(j[0]) + '-' + str(j[1])
  btmdict[mykey] = 0
  topdict[mykey] = 0

for i in btm:
  mykey = str(i[0]) + '-' + str(i[1])
  btmdict[mykey] += 1
for j in top:
  mykey = str(j[0]) + '-' + str(j[1])
  topdict[mykey] += 1

ans = 1
for i in btmdict:
  btmi = btmdict[i]
  topi = topdict[i]
  if btmi*topi >= 1:
    ans = ans * (pow(2, btmi, MOD) +pow(2, topi, MOD) -1) %MOD
  elif btmi == 0:
    ans = ans * pow(2, topi, MOD) %MOD
  else:
    ans = ans * pow(2, btmi, MOD) %MOD

ans = (ans +count00 -1) %MOD
print(ans)
