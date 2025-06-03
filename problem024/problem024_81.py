from collections import deque

def isPa(w,k,p):
    tr = 0
    c = 0
    d = deque(w)
    while(d):
        tmp = d.popleft()
        if(tmp > p):
            return False
        
        if( tr + tmp > p):
            tr = tmp
            c += 1
        else:
            tr += tmp
        if c+1>k:
            return False
    return True

def MaxInP(w,k,p):
    maxinp = 0
    tmp = 0
    d = deque(w)
    while(d):
        tmp += d.popleft();
        if(tmp > p):
            if(tmp > maxinp):
                maxinp = tmp
            tmp = 0
    return maxinp

n,k = [int(x) for x in input().split()]
w = deque()
for i in range(n):
    w.append(int(input()))
    
mean = int(sum(w)/k)
maxinp = MaxInP(w,k,mean)

if k == 1:
    print(mean)
else:
    minP = mean
    maxP = maxinp
    while(True):
        m = int ((minP + maxP)/2)
        if ( isPa(w,k,m) ):
            maxP = m
        else:
            minP = m
        if (minP+1 == maxP or minP == maxP):
            print(maxP)
            break