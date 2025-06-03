from heapq import *
from collections import deque

N,K,*A = map(int, open(0).read().split())
pos = []
zero = 0
neg = []
count = K
m = 1000000007
for x in A:
    if x > 0:
        pos.append(x)
    elif x == 0:
        zero += 1
    else:
        neg.append(x)
if K == N:
    ans = A[0] % m
    for x in A[1:]:
        ans = (ans*x) % m
    print(ans)
elif K % 2 == 1 and len(pos) == 0:
    if zero > 0:
        print(0)
    else:
        ai = [x * (-1) for x in A]
        heapify(ai)
        ans = (heappop(ai)*(-1)) % m
        for i in range(K-1):
            ans = (ans*heappop(ai)*(-1)) % m
        print(ans)
elif K > N - zero:
    print(0)
else:
    heapify(neg)
    ans = 1
    negpos = []
    for i in range(len(neg)//2):
        temp = heappop(neg)
        negpos.append(temp*heappop(neg))
    dnp = deque(negpos)
    posi = [x * (-1) for x in pos]
    heapify(posi)
    if len(posi) > 0:
        t1 = heappop(posi) * (-1)
    else:
        t1 = 1
    if len(posi) > 0:
        t2 = heappop(posi) * (-1)
    else:
        t2 = 1
    for i in range(K):
        if count > 1:
            if len(dnp) > 0:
                if t1 > dnp[0]:
                    if count > 2:
                        ans = (ans*t1) % m
                        t1 = t2
                        if len(posi) > 0:
                            t2 = heappop(posi) * (-1)
                        else:
                            t2 = 1
                        count -= 1
                    else:
                        if t2 == 1 and len(posi) == 0:
                            ans = (ans*dnp.popleft()) % m
                            count -= 2
                        else:
                            ans = (ans*t1) % m
                            t1 = t2
                            if len(posi) > 0:
                                t2 = heappop(posi) * (-1)
                            else:
                                t2 = 1
                            count -= 1
                else:
                    if t1 * t2 > dnp[0]:
                        if count != 3:
                            ans = (ans*t1*t2) % m
                            if len(posi) > 0:
                                t1 = heappop(posi) * (-1)
                            else:
                                t1 = 1
                            if len(posi) > 0:
                                t2 = heappop(posi) * (-1)
                            else:
                                t2 = 1
                            count -= 2
                        else:
                            if len(posi) > 0:
                                t3 = heappop(posi) * (-1)
                                M = max(t1*t2*t3,dnp[0]*t1)
                                ans = (ans*M) % m
                                break
                            else:
                                ans = (ans*dnp.popleft()*t1) % m
                                break
                    else:
                        ans = (ans*dnp.popleft()) % m
                        count -= 2
            else:
                ans = (ans*t1) % m
                if len(posi) > 0:
                    t1 = t2
                    t2 = heappop(posi) * (-1)
                else:
                    t1 = t2
                count -= 1
        elif count == 1:
            ans = (ans*t1) % m
            break
        else:
            break
    print(ans)