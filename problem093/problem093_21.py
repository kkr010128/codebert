import sys
sys.setrecursionlimit(10**7)

readline = sys.stdin.buffer.readline
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))

from itertools import accumulate

def sum_max(line,n_min,n_max):
    n = len(line)
    ac = list(accumulate([0]+line))
    l = 0
    r = n_min
    ans = ac[r]-ac[l]
    i  = 0
    if n_min>n_max:
        ans = 0
    elif n_min==n_max:
        for i in range(n-n_min+1):
            ans = max(ans,ac[i+n_min]-ac[i])
    else:
        while r!=n or i%2==1:
            if i%2==0:
                r = ac[r+1:l+n_max+1].index(max(ac[r+1:l+n_max+1])) + r+1
            else:
                l = ac[l+1:r-n_min+1].index(min(ac[l+1:r-n_min+1])) + l+1
            i+=1
            ans = max(ans,ac[r]-ac[l])
    return ans

def sum_min(line,n_min,n_max):
    n = len(line)
    ac = list(accumulate([0]+line))
    l = 0
    r = n_min
    ans = ac[r]-ac[l]
    i  = 0
    if n_min>n_max:
        ans = 0
    elif n_min==n_max:
        for i in range(n-n_min+1):
            ans = min(ans,ac[i+n_min]-ac[i])
    else:
        while r!=n or i%2==1:
            if i%2==0:
                r = ac[r+1:l+n_max+1].index(min(ac[r+1:l+n_max+1])) + r+1
            else:
                l = ac[l+1:r-n_min+1].index(max(ac[l+1:r-n_min+1])) + l+1
            i+=1
            ans = min(ans,ac[r]-ac[l])
    return ans

def circle_sum_max(circle,n_min,n_max):
    n = len(circle)
    s = sum(circle)
    if n_min>n_max:
        ans = 0
    else:
        ans = max(sum_max(circle,n_min,n_max), s-sum_min(circle,n-n_max,n-n_min))
    return ans

def circle_sum_min(circle,n_min,n_max):
    n = len(circle)
    s = sum(circle)
    if n_min>n_max:
        ans = 0
    else:
        ans = max(sum_min(circle,n_min,n_max), s-sum_max(circle,n-n_max,n-n_min))
    return ans
 
n,k = readints()
p = [x-1 for x in readints()]
c = readints()

circles = []
used = [0]*n

for i in range(n):
    if not used[i]:
        circles.append([c[i]])
        used[i] = 1
        j = p[i]
        while not used[j]:
            circles[-1].append(c[j])
            used[j] = 1
            j = p[j]

score = -10**20

for cir in circles:
    m = len(cir)
    a = sum(cir)
    if k>m:
        if a>0:
            score = max(score, (k//m)*a + circle_sum_max(cir,1,k%m), (k//m-1)*a + circle_sum_max(cir,1,m))
        else:
            score = max(score,circle_sum_max(cir,1,m))
    else:
        score = max(score,circle_sum_max(cir,1,k))

print(score)








