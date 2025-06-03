import math
N = int(input())
Alist = list(map(int,input().split()))
box = [0]*(10**6+1)
sign = math.gcd(Alist[0],Alist[1])
Amax = max(Alist[0],Alist[1])
for i in range(0,len(Alist)):
    A = Alist[i]
    sign = math.gcd(sign, A)
    Amax = max(Amax, A)
    box[A] += 1
setwise = (sign == 1)
pairwise = (sign == 1)
Amax = math.sqrt(Amax)+1
for i in range(2,10**6+1):
    if sum(box[i::i]) >1:
        pairwise = False
        break
if setwise:
    if pairwise:
        print('pairwise coprime')
    else:
        print('setwise coprime')
else:
    print('not coprime')